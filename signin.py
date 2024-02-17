import math

from model import Activity


def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # 地球平均半径，单位公里
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(math.radians(lat1)) * math.cos(
        math.radians(lat2)) * math.sin(dLon / 2) * math.sin(dLon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json


@csrf_exempt
@require_http_methods(["POST"])
def compare_location(request):
    data = json.loads(request.body)
    user_latitude = data.get('latitude')
    user_longitude = data.get('longitude')

    # 阈值设为1公里
    threshold_distance = 1  # km

    # 检索所有活动
    user = User.objects.get(pk=user_id)

    activities = Activity.objects.all()
    for activity in activities:
        distance = calculate_distance(user_latitude, user_longitude, activity.latitude, activity.longitude)
        if distance <= threshold_distance:
            # 找到一个距离用户足够近的活动，更新打卡状态
            ActivityCheckin.objects.update_or_create(
                user=user,
                activity=activity,
                defaults={'is_checked_in': True}
            )
            return JsonResponse(
                {'status': 'success', 'message': 'Sign in successfully'})

    # 如果没有找到任何匹配的活动
    return JsonResponse({'status': 'failed', 'message': 'Failed to sign in'})

