from django.shortcuts import render, get_object_or_404

from .models import Announcement  # 确保从你的模型文件中导入 Announcement


def list(request):
    announcements = Announcement.objects.order_by('date_start')
    return render(request, 'announcement/list.html', {'announcements': announcements})

def detail(request, title):
    # 使用 get_object_or_404 来获取特定公告或返回404
    announcement = get_object_or_404(Announcement, title=title)
    return render(request, "announcement/detail.html", {'announcement': announcement})
