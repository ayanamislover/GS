from django.shortcuts import render


def map_view(request):
    # 假设这些是从数据库或其他来源获取的经纬度
    target_latitude = 50.7260
    target_longitude = -3.5275
    context = {
        'target_latitude': target_latitude,
        'target_longitude': target_longitude,
    }
    return render(request, 'checkers/navigation.html', context)
