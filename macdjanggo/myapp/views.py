from django.shortcuts import render
from .models import leaderboard
# Create your views here.
# views.py

from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def user_dashboard(request):
    return render(request, 'user_dashboard.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def developer_dashboard(request):
    return render(request, 'developer_dashboard.html')

def user_leaderboard(request):
    users = leaderboard.objects.all()  # get the models' object

    # ordering using different keys
    score_leaderboard = sorted(users, key=lambda x: x.score, reverse=True)
    achievements_leaderboard = sorted(users, key=lambda x: x.achievements, reverse=True)
    login_days_leaderboard = sorted(users, key=lambda x: x.login_days, reverse=True)
    carbon_footprint_leaderboard = sorted(users, key=lambda x: x.carbon_footprint, reverse=True)

    return render(request, 'user_leaderboard.html', {
        'score_leaderboard': score_leaderboard,
        'achievements_leaderboard': achievements_leaderboard,
        'login_days_leaderboard': login_days_leaderboard,
        'carbon_footprint_leaderboard': carbon_footprint_leaderboard,
    })

def user_profile(request):
    return render(request, 'user_profile.html')

def developer_leaderboard(request):
    return render(request, 'developer_leaderboard.html')

def developer_profile(request):
    return render(request, 'developer_profile.html')

def user_management(request):
    return render(request, 'user_management.html')
