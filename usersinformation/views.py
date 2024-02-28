from django.shortcuts import get_object_or_404, render,redirect, reverse
from django.http import HttpResponse
from .models import PlayerProfile
from .forms import PlayerProfileForm, DisplayedAchievementsForm
from django.contrib import messages  # 引入 messages 模块
from django.contrib.auth.decorators import login_required
# Create your views here.

def player_profile_none(request):
    # 使用render函数渲染响应，指定模板文件和上下文数据（如果有）
    return render(request, 'usersinformation/player_profile_none.html')

    # 或者重定向到登录页面，假设登录页面的URL名称为'login'
    # return redirect('login')
#返回用户界面视图
#@login_required
#使用了 @login_required 装饰器，确保只有登录的用户才能访问这个页面。如果未登录的用户尝试访问，他们将被重定向到登录页面。


# 确保登录视图将用户ID保存在session中
def player_profile2(request,pk):
    # 从session中获取当前登录用户的ID

    # 获取与当前登录用户关联的PlayerProfile实例
    try:
        player_profile = PlayerProfile.objects.get(pk=pk)
        context = {'player_profile': player_profile}
        return render(request, 'usersinformation/player_profile.html', context)
    except PlayerProfile.DoesNotExist:
        # 如果找不到关联的PlayerProfile，可以渲染一个错误页面或者做其他处理
        # 例如，重定向到登录页面或显示错误信息
        context = {'error': 'Player profile not found.'}
        return render(request, 'usersinformation/error.html', context)


#测试，抓取对应昵称,显示用户界面
def detailnickname(request, nickname):
    # 通过昵称来获取 PlayerProfile 实例
    player_information = get_object_or_404(PlayerProfile, nickname=nickname)
    # 将获取到的用户信息传递给模板
    return render(request, "usersinformation/player_profile.html", {"player_information": player_information})


def player_profile(request, nickname):
    try:
        # 通过id来获取 PlayerProfile 实例
        player_information = get_object_or_404(PlayerProfile, nickname=nickname)
        # 获取所有成就
        all_achievements = player_information.achievements.all()
        # 从PlayerProfile关联的User实例获取邮箱信息
        #user_email = player_information.user.email  # 这里假设PlayerProfile有一个名为user的字段关联到User模型

        # 直接从实例调用方法获取解锁成就的数量
        unlocked_achievement_count = player_information.unlocked_achievement_count()
        # 获取用户选择展示的成就，如果没有，则默认展示所有成就中的前三个
        displayed_achievements = player_information.displayed_achievements.all()[:3] if player_information.displayed_achievements.exists() else all_achievements[:3]
        # 将获取到的用户信息和成就传递给模板
        return render(request, "usersinformation/player_profile.html", {
            "player_information": player_information,
            "all_achievements": all_achievements,
            "displayed_achievements": displayed_achievements,
            "unlocked_achievement_count":unlocked_achievement_count,
            #"user_email": user_
        })
    except PlayerProfile.DoesNotExist:
        # 如果找不到关联的PlayerProfile，可以渲染一个错误页面或者做其他处理
        # 例如，重定向到登录页面或显示错误信息
        context = {'error': 'Player profile not found.'}
        return render(request, 'usersinformation/error.html', context)


#定义编辑页面视图
def edit_player_profile(request, nickname):
    player_profile = get_object_or_404(PlayerProfile, nickname=nickname)
    # 如果请求是POST，处理表单数据
    if request.method == 'POST':
        profile_form = PlayerProfileForm(request.POST, request.FILES, instance=player_profile)
        #achievements_form = DisplayedAchievementsForm(request.POST, instance=player_profile)  # 新增成就表单
        achievements_form = DisplayedAchievementsForm(request.POST, instance=player_profile, user_nickname=nickname)#增加只显示已经解锁成就
        # 检查两个表单是否都有效
        if profile_form.is_valid() and achievements_form.is_valid():
            profile_form.save()
            achievements_form.save()  # 保存选择的成就
            messages.success(request, 'Profile and achievements updated successfully!')
            # return redirect('player_profile', nickname=player_profile.nickname)
            return redirect(reverse('usersinformation:player_profile', kwargs={"nickname":player_profile.nickname}))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        # 如果不是POST请求，初始化表单
        profile_form = PlayerProfileForm(instance=player_profile)
        #achievements_form = DisplayedAchievementsForm(instance=player_profile)  # 初始化成就表单
        achievements_form = DisplayedAchievementsForm(instance=player_profile, user_nickname=nickname)#增加用户主键

    # 传递两个表单到模板
    return render(request, 'usersinformation/edit_player_profile2.html', {
        'profile_form': profile_form,
        'achievements_form': achievements_form
    })
