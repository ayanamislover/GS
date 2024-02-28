from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from usersinformation.models import PlayerProfile

def user_leaderboard(request):
    # 获取按积分降序排列的 PlayerProfile 对象列表
    score_leaderboard = PlayerProfile.objects.order_by('-score')[:10]  # 获取前10名

    # 获取按成就数量降序排列的 PlayerProfile 对象列表
    achievement_leaderboard = PlayerProfile.objects.order_by('-achievement_count')[:10]  # 获取前10名

    # 将排行榜数据传递给模板
    context = {
        'score_leaderboard': score_leaderboard,
        'achievement_leaderboard': achievement_leaderboard,
    }
    return render(request, 'user_leaderboard.html', context)