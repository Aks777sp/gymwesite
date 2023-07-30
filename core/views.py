from django.shortcuts import render
from .models import Gym
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from members.models import Post

def main_view(request):
    post_list = Post.objects.all().order_by('-date_created')  # get all posts, newest first
    page = request.GET.get('page', 1)  # get the current page number

    paginator = Paginator(post_list, 5)  # Show 5 posts per page

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    core = Gym.objects.first()  # assuming there's only one row in the Core table

    return render(request, 'main.html', {'core': core, 'page': page, 'posts': posts})


def contact_view(request):
    gym = Gym.objects.first()  # or use get if you have a specific gym you want to display
    return render(request, 'contact.html', {'gym': gym})



def core_processor(request):
    core = Gym.objects.first()  # or however you get your core object
    return {'core': core}