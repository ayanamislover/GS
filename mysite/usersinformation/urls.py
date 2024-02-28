from django.urls import path

from . import views

urlpatterns = [
    #/usersinformation/edit_profile/nickname/ to jump to the user information edit screen by nickname information
    path('edit_player_profile/<str:nickname>/', views.edit_player_profile, name='edit_player_profile'),
    # /usersinformation/nickname/ to jump to the user information screen by nickname information
    path("<str:nickname>/", views.detailnickname, name="detailnickname"),
    #main view
    path('player_profile/<str:nickname>/', views.player_profile, name='player_profile'),  # 添加这个路径
]