from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import PlayerProfile
from .forms import PlayerProfileForm
from django.contrib import messages  # 引入 messages 模块
from django.contrib.auth.decorators import login_required
# Create your views here.


#返回用户界面视图
#@login_required
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
def detailnickname(request, nickname):
    # 通过昵称来获取 PlayerProfile 实例
    player_information = get_object_or_404(PlayerProfile, nickname=nickname)
    # 将获取到的用户信息传递给模板
    return render(request, "usersinformation/player_profile.html", {"player_information": player_information})


def detailid(request, pk):
    # 通过id来获取 PlayerProfile 实例
    player_information = get_object_or_404(PlayerProfile, pk=pk)
    # 将获取到的用户信息传递给模板
    return render(request, "usersinformation/player_profile.html", {"player_information": player_information})


#定义编辑页面视图
def edit_player_profile(request, pk):
    player_profile = get_object_or_404(PlayerProfile, pk=pk)
    if request.method == 'POST':
        form = PlayerProfileForm(request.POST, request.FILES, instance=player_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')  # 添加成功消息
            return redirect('detailid', pk=player_profile.pk)
        else:
            # 如果表单不合法，添加一条错误消息
            messages.error(request, 'Please correct the error below.')
    else:
        form = PlayerProfileForm(instance=player_profile)
    return render(request, 'usersinformation/edit_player_profile2.html', {'form': form})
