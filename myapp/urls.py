# urls.py

from django.urls import path
from myapp import views

urlpatterns = [
    path('home/<str:nickname>/', views.home, name='home'),
    path('admin1/', views.admin_dashboard, name='admin_dashboard'),
    path('developer/', views.developer_dashboard, name='developer_dashboard'),
    path('user/leaderboard/', views.user_leaderboard, name='user_leaderboard'),
    path('developer/leaderboard/', views.developer_leaderboard, name='developer_leaderboard'),
    path('developer/profile/<str:nickname>/', views.developer_profile, name='developer_profile'),
    path('developer/user_management/', views.user_management, name='user_management'),
]
