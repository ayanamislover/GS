from django.shortcuts import render,reverse,redirect
from django.db.models import F
from usersinformation.models import PlayerProfile

def SceneSelect(request, loc_id,nickname):
    # First, update the score
    PlayerProfile.objects.filter(nickname=nickname).update(score=F('score') + 2)

    # Then, re-fetch the player object to get the updated score
    try:
        player = PlayerProfile.objects.get(nickname=nickname)
        score = player.score
    except PlayerProfile.DoesNotExist:
        score = 0  # If the player does not exist, you can choose how to handle it; here, we assume the score is 0

    # Pass the nickname and score to the template
    context = {
        'nickname': nickname,
        'score': score,
    }
    return render(request, "MeadowAd.html", context=context)


def MeadowAd(request, nickname):
    # First, update the score
    PlayerProfile.objects.filter(nickname=nickname).update(score=F('score') + 2)

    # Then, re-fetch the player object to get the updated score
    try:
        player = PlayerProfile.objects.get(nickname=nickname)
        score = player.score
    except PlayerProfile.DoesNotExist:
        score = 0  # If the player does not exist, you can choose how to handle it; here, we assume the score is 0

    # Pass the nickname and score to the template
    context = {
        'nickname': nickname,
        'score': score,
    }
    return render(request, "MeadowAd.html", context=context)
