from django.shortcuts import render,redirect
from django.urls import reverse
# Create your views here.
# views.py

from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def user_dashboard(request):
    return render(request, 'user_dashboard.html')

def user_leaderboard(request):
    return redirect(reverse('user_leaderboard'))

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def developer_dashboard(request):
    return render(request, 'developer_dashboard.html')

def user_profile(request):
    return render(request, 'user_profile.html')

def developer_leaderboard(request):
    return render(request, 'developer_leaderboard.html')

def developer_profile(request):
    return render(request, 'developer_profile.html')

def user_management(request):
    return render(request, 'user_management.html')
