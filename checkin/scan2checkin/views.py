import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from .models import Activity
from .location_utils import is_within_distance


def scan_qr_code(request):
    return render(request, 'scan_qr_code.html')


@csrf_exempt
def process_qr_code(request, qr_code):
    if qr_code.startswith('ACT'):
        return check_in(request, qr_code)


#  elif qr_code.startswith('ANS'):
#     return answer(request, qr_code)
#   else:
#       return JsonResponse({'error': 'Invalid QR code'}, status=400)

def check_in(request, qr_code):
    activity = get_object_or_404(Activity, code=qr_code)
    # 将活动代码传递给模板
    return render(request, 'test.html', {'activity_code': activity.code})


@csrf_exempt
def check_location(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user_lat = data['latitude']
        user_lon = data['longitude']
        activity_code = data['activity_code']

        activity = get_object_or_404(Activity, code=activity_code)
        if is_within_distance(user_lat, user_lon, activity.latitude, activity.longitude, threshold=10):
            #     request.user.profile.score += 2
            return JsonResponse({'status': 'success', 'message': 'Check in success'})
        else:
            return JsonResponse({'status': 'failure', 'message': 'Fail, out of range'})
    else:
        return JsonResponse({'status': 'failure', 'message': 'Illegal requests'}, status=400)

# def answer(qr_code):
# 在这里处理answer逻辑
#   return JsonResponse({'result': f'Answered with {qr_code}'})
