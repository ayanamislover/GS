from django.urls import path

from . import views

urlpatterns = [
    #/usersinformation/edit_profile/id/，靠id信息跳转到用户信息编辑界面
    path('edit_player_profile/<str:nickname>/', views.edit_player_profile, name='edit_player_profile'),
    #注意id匹配放置在昵称匹配之前，因为str字符串包括数字
    #/usersinformaiton/id/,靠id信息跳转到用户信息界面
   # path("<int:pk>/", views.detailid, name="detailid"),
    # /usersinformation/昵称/，靠昵称信息跳转到用户信息界面
    path("<str:nickname>/", views.detailnickname, name="detailnickname"),
    #主视图，/usesinformaiton/留着说不定和主界面模块连接
    path('player_profile/<str:nickname>/', views.player_profile, name='player_profile'),  # 添加这个路径
]