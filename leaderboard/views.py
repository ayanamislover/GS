from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from usersinformation.models import PlayerProfile
from decorate import login_requiredforuser
@login_requiredforuser
def user_leaderboard(request):
    # Gets a list of PlayerProfile objects in descending order of credits
    score_leaderboard = PlayerProfile.objects.order_by('-score')[:10]  # Get the top 10

    # Gets a list of PlayerProfile objects in descending order by number of achievements
    carbon_leaderboard = PlayerProfile.objects.order_by('-carbon')[:10]  # Get the top 10

    # Pass leaderboard data to the template
    context = {
        'score_leaderboard': score_leaderboard,
        'carbon_leaderboard': carbon_leaderboard,
    }
    return render(request, 'user_leaderboard.html', context)
