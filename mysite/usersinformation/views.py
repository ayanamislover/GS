from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import PlayerProfile
from django.contrib.auth.decorators import login_required
# Create your views here.


#返回用户界面视图
@login_required
#使用了 @login_required 装饰器，确保只有登录的用户才能访问这个页面。如果未登录的用户尝试访问，他们将被重定向到登录页面。
def player_profile(request):
    try:
        #查询与当前用户关联的PlayProfile模型实列
        player_information = PlayerProfile.objects.get(user=request.user)
    except PlayerProfile.DoesNotExist:
        return HttpResponse("User does not exist.", status=404)
    context = {"player_information": player_information}
    return render(request, "usersinformation/player_profile.html", context)


#测试，抓取对应昵称,显示用户界面
def detail(request, nickname):
    # 通过昵称来获取 PlayerProfile 实例
    player_information = get_object_or_404(PlayerProfile, nickname=nickname)
    # 将获取到的用户信息传递给模板
    return render(request, "usersinformation/player_profile.html", {"player_information": player_information})