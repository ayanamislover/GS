from django.http import JsonResponse
from model import Activity

def check_in(request):
    activity_id = request.GET.get('activityId')  # 通过GET请求发送活动ID
    try:
        activity = Activity.objects.get(pk=activity_id)
        activity.is_checked_in = True  # 更新打卡状态
        activity.save()
        return JsonResponse({'status': 'success', 'message': '打卡成功'})
    except Activity.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': '活动不存在'})
