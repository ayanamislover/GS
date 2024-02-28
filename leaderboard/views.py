from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from usersinformation.models import PlayerProfile

def user_leaderboard(request):
    # Gets a list of PlayerProfile objects in descending order of credits
    score_leaderboard = PlayerProfile.objects.order_by('-score')[:10]  # Get the top 10

    # Gets a list of PlayerProfile objects in descending order by number of achievements
    achievement_leaderboard = PlayerProfile.objects.order_by('-achievement_count')[:10]  # Get the top 10

    # Pass leaderboard data to the template
    context = {
        'score_leaderboard': score_leaderboard,
        'achievement_leaderboard': achievement_leaderboard,
    }
    return render(request, 'user_leaderboard.html', context)
