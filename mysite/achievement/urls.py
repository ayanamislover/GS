from django.urls import path

from . import views

urlpatterns = [
    #/usersinformation/edit_profile/id/，靠id信息跳转到用户信息编辑界面
    #path('edit_profile/<int:pk>/', views.edit_player_profile, name='edit_player_profile'),
    #注意id匹配放置在昵称匹配之前，因为str字符串包括数字
    #/achievement/id/,靠id信息跳转到用户成就信息界面
    #path("<int:pk>/", views.detail, name="detail"),
    # /usersinformation/昵称/，靠昵称信息跳转到用户信息界面
    #path("<str:nickname>/", views.detailnickname, name="detailnickname"),
    #主视图，/achievement/留着说不定和主界面模块连接
    path("", views.achievement_detail, name="ahchievement_detail"),
]