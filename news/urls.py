from django.urls import path
from .views import post_news

urlpatterns = [
    path('post/', post_news, name='post_news'),
]
