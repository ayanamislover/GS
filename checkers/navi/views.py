import json
from django.shortcuts import render
from .models import Checker, player_profile
import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .location_utils import is_within_distance
import datetime
from django.utils import timezone
from django.urls import reverse
include = ('answerquestion.views', 'answerquestion', 'answerquestion.urls')
from answerquestion.views import series_detail
# from usersinformation.models import PlayerProfile
from django.http import HttpResponseRedirect


# from answerquestion.views import series_detail2,results_page2

# def can_start_new_game(nickname):
#     player = PlayerProfile.nickname
#     now = timezone.now()
#     # 如果用户从未开始过游戏则可以开始新游戏
#     if not PlayerProfile.last_game_start:
#         return True
#
#         # 如果已经过去了7天，则可以开始新游戏
#     if (datetime.now().date() - PlayerProfile.last_game_start) >= datetime.timedelta(days=7):
#         return True
#     elif (datetime.now().date() - PlayerProfile.last_game_start) < datetime.timedelta(
#             days=7) and PlayerProfile.verified_locations_count == 3:
#         print('You have already verified 3 locations this week. You can start a new game next week.')
#         return False
#     else:
#         print('You have already finished a game this week. You can start a new game next week.')
#     return False


def checkersgame(request, nickname):
    # user = PlayerProfile.nickname
    # # 检查会话中是否已经存储了位置
    # if can_start_new_game(user):
    #     # 重置用户的游戏信息
    #     user.last_game_start = timezone.now()
    #     user.verified_locations_count = 0
    # else:
    #     print('You are not allowed to start a new game yet.')

    del request.session['target_id']
    if 'target_id' not in request.session:
        # 如果没有存储，则随机选择一个新位置
        count = Checker.objects.count()
        random_index = random.randint(0, count - 1)
        print('Random:', random_index, 'Total count:', count)

        target = Checker.objects.all()[random_index]
        # 将选中的位置的ID存储在会话中
        request.session['target_id'] = target.id
    else:
        # 如果已经存储了位置，就从会话中获取
        target_id = request.session['target_id']
        target = Checker.objects.get(id=target_id)

    target_latitude = target.latitude
    target_longitude = target.longitude
    nickname = nickname
    context = {
        'nickname': nickname,
        'target_latitude': target_latitude,
        'target_longitude': target_longitude,
    }

    return render(request, 'navigation.html', context)


@csrf_exempt
@require_http_methods(["POST"])
def check_location(request, nickname):
    print('Request received:', request.body)
    data = json.loads(request.body.decode('utf-8'))
    user_lat = data['user_latitude']
    user_lon = data['user_longitude']
    target_lat = data['target_latitude']
    target_lon = data['target_longitude']
    try:
        # 检查用户是否在目标位置的阈值范围内
        if is_within_distance(user_lat, user_lon, target_lat, target_lon, threshold=11):
            new_target = get_new_random_target(request.session.get('target_id'))
            request.session['target_id'] = new_target.id
            request.session.save()
            print('Random index:', request.session['target_id'])
            redirect_url = reverse('ans:series_detail', kwargs={'series_id': 1, 'nickname': nickname})
            print('Check-in successful, redirecting to:', redirect_url)
            response_data = {
                'status': 'success',
                'redirect_url': redirect_url
            }
            return JsonResponse(response_data)
        else:
            # 如果用户不在目标范围内，返回失败消息
            return JsonResponse({'status': 'failure', 'message': 'Check-in failed, out of range.'})
    except KeyError:
        # 如果POST数据不完整，返回错误消息
        return JsonResponse({'status': 'failure', 'message': 'Incomplete data provided.'})


def get_new_random_target(exclude_id):
    # 获取除了exclude_id之外的所有Checker对象的ID列表
    ids = Checker.objects.exclude(id=exclude_id).values_list('id', flat=True)
    ids_list = list(ids)

    # 如果列表为空，返回None
    if not ids_list:
        return None

    # 从列表中随机选择一个ID
    random_id = random.choice(ids_list)

    # 根据随机选择的ID获取Checker对象
    return Checker.objects.get(id=random_id)
