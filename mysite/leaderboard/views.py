from django.shortcuts import render
from .models import leaderboard
# Create your views here.
from django.http import HttpResponse

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