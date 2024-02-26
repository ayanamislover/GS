from django.shortcuts import render,redirect
from django.urls import reverse
from usersinformation.views import player_profile
# Create your views here.
# views.py

from django.shortcuts import render, redirect

def home(request, nickname):
    # 创建上下文字典，将变量传递给模板
    context = {
        'nickname': nickname
    }
    # 传递上下文到模板
    return render(request, 'home.html', context)

def user_dashboard(request):
    return render(request, 'user_dashboard.html')

def user_leaderboard(request):
    return redirect(reverse('user_leaderboard'))

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def developer_dashboard(request):
    return render(request, 'developer_dashboard.html')

def user_profile(request):
    return redirect(reverse('usersinformation:player_profile', kwargs={"nickname":player_profile.nickname}))

def developer_leaderboard(request):
    return render(request, 'developer_leaderboard.html')

def developer_profile(request):
    return render(request, 'developer_profile.html')

def user_management(request):
    return render(request, 'user_management.html')

#去achievement的视图
def to_achievement(request):
    # 假设 achievement_detail 视图不需要任何参数
    return redirect('achievement:achievement_detail')