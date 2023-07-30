
from .forms import MemberRegistrationForm, PostForm


def register(request):
    if request.method == 'POST':
        form = MemberRegistrationForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            password = form.cleaned_data.get('password')
            member.password = hashlib.sha256(password.encode()).hexdigest()  # hash password before storing
            member.save()

            member = Member.objects.get(email=member.email)
            request.session["member_id"] = member.id

            return redirect('profile')
    else:
        form = MemberRegistrationForm()
    return render(request, 'members/register.html', {'form': form})



def profile(request):
    # Fetch the member ID from the session.
    member_id = request.session.get("member_id")

    # If the ID is None, then the user is not logged in.
    if member_id is None:
        return redirect("login")

    # Fetch the member object from the database.
    try:
        member = Member.objects.get(id=member_id)
    except Member.DoesNotExist:
        # If no member exists with this ID, the session data is out of sync with the database.
        # Clear the session and redirect the user to the login page.
        del request.session["member_id"]
        return redirect("login")
    print(f"Email: {member.email}")  # Log email
    print(f"Entered password: {member.password}")
    print(f"name: {member.first_name}")
    # Render the profile page, passing in the member object.
    return render(request, "members/profile.html", {"member": member})



from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .models import Member
import hashlib


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        print(f"Email: {email}")  # Log email
        print(f"Entered password: {password}")  # Log entered password
        print(f"Hashed password: {password_hash}")  # Log hashed password

        try:
            member = Member.objects.get(email=email)
        except ObjectDoesNotExist:
            messages.error(request, "Invalid email or password")
            return redirect("login")

        print(f"member password: {member.password}")
        if password_hash == member.password:
            request.session["member_id"] = member.id
            return redirect("profile")
        else:
            messages.error(request, "Invalid password")
            return redirect("login")

    else:
        return render(request, "members/login.html")


from .forms import MemberUpdateForm


def member_update_view(request):
    member_id = request.session.get("member_id")
    member = Member.objects.get(pk=member_id)

    if request.method == 'POST':
        form = MemberUpdateForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = MemberUpdateForm(instance=member)

    return render(request, 'members/edit_profile.html', {'form': form})


def member_processor(request):
    member_id = request.session.get('member_id', None)
    if member_id:
        member = Member.objects.get(id=member_id)
        return {'member': member}
    return {}

def logout_view(request):
    if 'member_id' in request.session:
        del request.session['member_id']
    return redirect('main_view')




def post_create(request):
    # Check if user is logged in and is a staff member
    if 'member_id' in request.session:
        member_id = request.session['member_id']
        member = Member.objects.get(id=member_id)  # get the Member instance
        if member.is_staff:
            if request.method == "POST":
                form = PostForm(request.POST)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.member = member
                    post.save()
                    return redirect('main_view')
            else:
                form = PostForm()
            return render(request, 'post_news.html', {'form': form})
    # Redirect non-staff users or non-logged in users to main page
    return redirect('main_view')
