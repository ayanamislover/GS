from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from django.urls import path
from .models import Achievement
from usersinformation.models import AchievementAndUser, PlayerProfile
from web.models import User
from django.forms.models import model_to_dict
from django.contrib import messages
from decorate import login_requiredforuser

# Create your views here.
#Achievement system detail screen view
@login_requiredforuser
def detail(request, pk):
    # Getting an Achievement instance by nickname
    achievement_detail = get_object_or_404(Achievement, pk=pk)
    # Pass the fetched user information to the template
    return render(request, "achievement/achievement_detail.html", {"achievement_detail": achievement_detail})

@login_requiredforuser
def achievement_detail(request):
    # Get all achievements
    username = request.session.get("user_username")
    # Get user
    # user = User.objects.get(username=username)
    # print("User's information：", model_to_dict(user))
    # print("User's profile：", user.player_profile)
    
    player_profile = PlayerProfile.objects.get(nickname=username)
    result = []
    achievement_detail = Achievement.objects.all()
    for achievement in achievement_detail:
        achievement_dict = model_to_dict(achievement)
        print(achievement)
        # Find the relevant achievement
        record = AchievementAndUser.objects.filter(achievement=achievement, user=player_profile).first()
        if record:
            print("Find!：",  record.created_at)
            achievement_dict["create_time"] = record.created_at
            achievement_dict["state"] = True
        else:
            print("Not find!!!!")
            achievement_dict["create_time"] = ''
            achievement_dict["state"] = False
        result.append(achievement_dict)
    # return render(request, "achievement/achievement_detail.html", {'achievement_detail': achievement_detail})
    return render(request, "achievement/achievement_detail.html", {'achievement_detail': result})

