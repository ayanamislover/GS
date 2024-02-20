# checkin_views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .location_utils import is_within_distance
from model import Activity, User, ActivityCheckin

@csrf_exempt
@require_http_methods(["POST"])
def compare_location(request):
    data = json.loads(request.body)
    user_latitude = data.get('latitude')
    user_longitude = data.get('longitude')
    user_id = data.get('user_id')  # 假设请求中包含用户ID

    threshold_distance = 1  # km 阈值设为1公里

    # 检索所有活动
    user = User.objects.get(pk=user_id)
    activities = Activity.objects.all()
    for activity in activities:
        if is_within_distance(user_latitude, user_longitude, activity.latitude, activity.longitude, threshold_distance):
            # 找到一个距离用户足够近的活动，更新打卡状态
            ActivityCheckin.objects.update_or_create(
                user=user,
                activity=activity,
                defaults={'is_checked_in': True}
            )
            return JsonResponse({'status': 'success', 'message': 'Sign in successfully'})

    # 如果没有找到任何匹配的活动
    return JsonResponse({'status': 'failed', 'message': 'Failed to sign in'})
