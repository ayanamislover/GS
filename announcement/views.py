from django.shortcuts import render, get_object_or_404

import announcement


def title(request):
    return render(request, 'title.html')


# 公告列表视图
def list(request):
    announcements =announcement.objects.all().order_by('start_time')
    return render(request,'announcement/list.html')

# 公告详情视图
def detail(request):
    announcement_detail = get_object_or_404(announcement)
    return render(request,'announcement/detail.html')









