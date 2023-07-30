from django.urls import path
from . import views
from .views import login_view, member_update_view

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', login_view, name='login'),
    path('profile/edit/', member_update_view, name='edit_profile'),
    path('logout/', views.logout_view, name='logout'),


]