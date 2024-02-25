from django.shortcuts import get_object_or_404, render,redirect
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
def detailnickname(request, nickname):
    # 通过昵称来获取 PlayerProfile 实例
    player_information = get_object_or_404(PlayerProfile, nickname=nickname)
    # 将获取到的用户信息传递给模板
    return render(request, "usersinformation/player_profile.html", {"player_information": player_information})


def detailid(request, pk):
    # 通过id来获取 PlayerProfile 实例
    player_information = get_object_or_404(PlayerProfile, pk=pk)
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


#定义编辑页面视图
def edit_player_profile(request, pk):
    player_profile = get_object_or_404(PlayerProfile, pk=pk)
    # 如果请求是POST，处理表单数据
    if request.method == 'POST':
        profile_form = PlayerProfileForm(request.POST, request.FILES, instance=player_profile)
        #achievements_form = DisplayedAchievementsForm(request.POST, instance=player_profile)  # 新增成就表单
        achievements_form = DisplayedAchievementsForm(request.POST, instance=player_profile, user_pk=pk)#增加只显示已经解锁成就
        # 检查两个表单是否都有效
        if profile_form.is_valid() and achievements_form.is_valid():
            profile_form.save()
            achievements_form.save()  # 保存选择的成就
            messages.success(request, 'Profile and achievements updated successfully!')
            return redirect('detailid', pk=player_profile.pk)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        # 如果不是POST请求，初始化表单
        profile_form = PlayerProfileForm(instance=player_profile)
        #achievements_form = DisplayedAchievementsForm(instance=player_profile)  # 初始化成就表单
        achievements_form = DisplayedAchievementsForm(instance=player_profile, user_pk=pk)#增加用户主键

    # 传递两个表单到模板
    return render(request, 'usersinformation/edit_player_profile2.html', {
        'profile_form': profile_form,
        'achievements_form': achievements_form
    })
