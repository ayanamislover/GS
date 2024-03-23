from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from django.shortcuts import render, redirect
from usersinformation.models import PlayerProfile
from decorate import login_requiredforuser
@login_requiredforuser
def home(request,nickname):
    player_information = get_object_or_404(PlayerProfile, nickname=nickname)
    return render(request, "home.html", {"player_information": player_information})
@login_requiredforuser
def user_leaderboard(request):
    return redirect(reverse('user_leaderboard'))
@login_requiredforuser
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
@login_requiredforuser
def developer_dashboard(request):
    return render(request, 'developer_dashboard.html')
@login_requiredforuser
def developer_leaderboard(request):
    return render(request, 'developer_leaderboard.html')
@login_requiredforuser
def developer_profile(request):
    return render(request, 'developer_profile.html')
@login_requiredforuser
def user_management(request):
    return render(request, 'user_management.html')
