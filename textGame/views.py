from django.shortcuts import render,reverse,redirect
from django.db.models import F
from usersinformation.models import PlayerProfile

def SceneSelect(request, loc_id,nickname):

   if loc_id==1:
       # 首先更新分数
       PlayerProfile.objects.filter(nickname=nickname).update(score=F('score') + 2)

       # 然后重新获取玩家对象来获取更新后的分数
       try:
           player = PlayerProfile.objects.get(nickname=nickname)
           score = player.score
       except PlayerProfile.DoesNotExist:
           score = 0  # 如果玩家不存在，你可以选择如何处理，这里我们假设分数为0

       # 将昵称和分数传递给模板
       context = {
           'nickname': nickname,
           'score': score,
       }
       return render(request, "MeadowAd.html", context=context)



def MeadowAd(request, nickname):
    # 首先更新分数
    PlayerProfile.objects.filter(nickname=nickname).update(score=F('score') + 2)

    # 然后重新获取玩家对象来获取更新后的分数
    try:
        player = PlayerProfile.objects.get(nickname=nickname)
        score = player.score
    except PlayerProfile.DoesNotExist:
        score = 0  # 如果玩家不存在，你可以选择如何处理，这里我们假设分数为0

    # 将昵称和分数传递给模板
    context = {
        'nickname': nickname,
        'score': score,
    }
    return render(request, "MeadowAd.html", context=context)
