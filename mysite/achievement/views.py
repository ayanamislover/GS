from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import Achievement


from django.contrib import messages  # 引入 messages 模块

# Create your views here.
#成就系统详情界面视图
def detail(request, pk):
    # 通过昵称来获取 Achievement 实例
    achievement_detail = get_object_or_404(Achievement, pk=pk)
    # 将获取到的用户信息传递给模板
    return render(request, "achievement/achievement_detail.html", {"achievement_detail": achievement_detail})


def achievement_detail(request):
    # 获取所有成就
    achievement_detail = Achievement.objects.all()
    #传递信息给模板
    return render(request, "achievement/achievement_detail.html", {'achievement_detail': achievement_detail})
