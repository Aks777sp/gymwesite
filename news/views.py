from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewsForm

def post_news(request):
    if not request.member.is_staff:
        return redirect('main_view')  # Or another appropriate view
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.posted_by = request.member
            news.save()
            return redirect('news_posted')  # Or another appropriate view
    else:
        form = NewsForm()
    return render(request, 'news/post_news.html', {'form': form})
