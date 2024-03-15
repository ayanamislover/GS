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

def checkersgame(request, nickname):
    if 'target_id' not in request.session:
        # if not request.session.get('target_id'):
        count = Checker.objects.count()
        # select a random location from the database
        random_index = random.randint(0, count - 1)
        print('Random:', random_index, 'Total count:', count)
        # select a random location from the database
        target = Checker.objects.all()[random_index]
        # store the location in the session
        request.session['target_id'] = target.id
    else:
        # if the session already contains a location, retrieve it.
        target_id = request.session['target_id']
        target = Checker.objects.get(id=target_id)

    # retrieve the latitude and longitude of the target location
    target_latitude = target.latitude
    target_longitude = target.longitude
    nickname = nickname
    tag = target.tag
    picture = target.picture
    overview = target.overview
    location_name = target.location_name
    context = {
        'nickname': nickname,
        'target_latitude': target_latitude,
        'target_longitude': target_longitude,
        'tag': tag,
        'picture': picture,
        'overview': overview,
        'loc': location_name
    }
    # return the navigation page with the target location and the user's nickname.
    return render(request, 'navigation.html', context)


@csrf_exempt
@require_http_methods(["POST"])
def check_location(request, nickname):
    print('Request received:', request.body)
    data = json.loads(request.body.decode('utf-8'))
    # collect the user's location and the target location from the request
    user_lat = data['user_latitude']
    user_lon = data['user_longitude']
    target_lat = data['target_latitude']
    target_lon = data['target_longitude']
    try:

        if is_within_distance(user_lat, user_lon, target_lat, target_lon, threshold=11):
            # If the user is within the target range, select a new random target and return a success message
            new_target = get_new_random_target(request.session.get('target_id'))
            request.session['target_id'] = new_target.id
            request.session.save()
            print('Random index:', request.session['target_id'])
            # update the user's verified locations count
            redirect_url = reverse('ans:series_detail', kwargs={'series_id': 1, 'nickname': nickname})
            # redirect to the answerquestion app page
            print('Check-in successful, redirecting to:', redirect_url)
            response_data = {
                'status': 'success',
                'redirect_url': redirect_url
            }
            return JsonResponse(response_data)
        else:
            # If the user is not within the target range, return a failure message
            return JsonResponse({'status': 'failure', 'message': 'Check-in failed, out of range.'})
    except KeyError:
        # If the request does not contain the required data, return a failure message
        return JsonResponse({'status': 'failure', 'message': 'Incomplete data provided.'})


def get_new_random_target(exclude_id):
    # Get a list of all the IDs in the database
    ids = Checker.objects.exclude(id=exclude_id).values_list('id', flat=True)
    ids_list = list(ids)

    # If the list is empty, return None
    if not ids_list:
        return None

    # Select a random ID from the list
    random_id = random.choice(ids_list)

    # Return the Checker object with the selected ID
    return Checker.objects.get(id=random_id)
