from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import announcement



# 公告列表视图
def list(request):
    announcements = announcement.objects.all().order_by('start_time')  # 获取所有公告并按开始时间排序
    context = {"announcements":  announcements}
    return render(request, "announcement/list.html", context)


# 公告详情视图
def detail(request, announcement_id):
    # 使用announcement_id获取特定的公告实例，如果找不到则返回404
    announcemen = get_object_or_404(announcement, pk=announcement_id)
    context = {
        'announcemen': announcemen,  # 将公告实例放入上下文中
    }
    return render(request, 'announcement/detail.html', context)  # 将上下文传递给模板









