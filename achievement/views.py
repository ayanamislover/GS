from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from django.urls import path
from .models import Achievement
from usersinformation.models import AchievementAndUser, PlayerProfile
from web.models import User
from django.forms.models import model_to_dict
from django.contrib import messages

# Create your views here.
#Achievement system detail screen view
def detail(request, pk):
    # Getting an Achievement instance by nickname
    achievement_detail = get_object_or_404(Achievement, pk=pk)
    # Pass the fetched user information to the template
    return render(request, "achievement/achievement_detail.html", {"achievement_detail": achievement_detail})


def achievement_detail(request):
    # Get all achievements
    username = request.session.get("user_username")
    # 获取用户
    # user = User.objects.get(username=username)
    # print("对应的用户信息：", model_to_dict(user))
    # print("对应的用户信息：", user.player_profile)
    # 获取用户
    player_profile = PlayerProfile.objects.get(nickname=username)
    result = []
    achievement_detail = Achievement.objects.all()
    for achievement in achievement_detail:
        achievement_dict = model_to_dict(achievement)
        print(achievement)
        # 查找关联的成就记录
        record = AchievementAndUser.objects.filter(achievement=achievement, user=player_profile).first()
        if record:
            print("找到了相关的成就记录：",  record.created_at)
            achievement_dict["create_time"] = record.created_at
            achievement_dict["state"] = True
        else:
            print("没有找到相关的成就记录")
            achievement_dict["create_time"] = ''
            achievement_dict["state"] = False
        result.append(achievement_dict)
    # return render(request, "achievement/achievement_detail.html", {'achievement_detail': achievement_detail})
    return render(request, "achievement/achievement_detail.html", {'achievement_detail': result})

