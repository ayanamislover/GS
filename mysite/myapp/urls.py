# urls.py

from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.user_dashboard, name='user_dashboard'),
    path('admin1/', views.admin_dashboard, name='admin_dashboard'),
    path('developer/', views.developer_dashboard, name='developer_dashboard'),
    path('user/profile/', views.user_profile, name='user_profile'),
    path('user/leaderboard/', views.user_leaderboard, name='user_leaderboard'),
    path('developer/leaderboard/', views.developer_leaderboard, name='developer_leaderboard'),
    path('developer/profile/', views.developer_profile, name='developer_profile'),
    path('developer/user_management/', views.user_management, name='user_management'),
]
