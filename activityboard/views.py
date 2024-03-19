import cv2
from django.urls import reverse
import numpy as np
import base64
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseBadRequest, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from io import BytesIO
import qrcode
from django.db.models import F
from activityboard.models import  QuizSession,Location
from aM.models import Activity
from usersinformation.models import PlayerProfile
from answerquestion.models import Series
from math import radians, cos, sin, asin, sqrt
# Create your views here.



def activity_join(request):
    activities = Activity.objects.all()  # 获取所有活动
    return render(request, 'activity_join.html', {'activities': activities})


def generate_qrcode(request,series_id):
    if series_id is None:
        # Handle situations where there is no series_id 
        return HttpResponse("No series_id provided", status=400)
    # Create a QR Code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Set the data to be encoded (this can be any information you want to include in the QR Code)
    targeturl=reverse('enternickname',kwargs={'series_id':series_id})
    qr.add_data(targeturl)  # Replace this with your answer page URL
    qr.make(fit=True)
    # Create an image object and render the QR Code into the image
    img = qr.make_image(fill_color="black", back_color="white")
    # Save the image to a BytesIO object
    buffer = BytesIO()
    img.save(buffer)
    # Return the image to the client
    return HttpResponse(buffer.getvalue(), content_type="image/png")

def enternickname(request,series_id):
    series = get_object_or_404(Series, pk=series_id)
    if request.method == "POST":
        nickname = request.POST.get("nickname")
        if PlayerProfile.objects.filter(nickname=nickname).exists():
            # If the nickname exists, redirect to the target URL
            target_url_name=reverse('ans:series_detail',kwargs={'series_id': series_id, 'nickname': nickname})
            return redirect(target_url_name)  # Be sure to replace "target_url_name" with the name of your target URL
        else:
            # If the nickname does not exist, you can display an error message or perform another operation
            return render(request, "enternickname.html", {"error": "Nickname not found."})
    else:
        # If it is a GET request, the input form is displayed
        return render(request,'enternickname.html')



def scan_qr(request,series_id):
    location1=Activity.objects.get(series_id=series_id).location
    print(location1)
    try:
        location = Location.objects.get(name=location1)
    except Location.DoesNotExist:
        location = None
    context = {
        'location': location
    }
    return render(request, 'scan_qr.html', context)
    
def quiz_leaderboard(request,nickname,additional_score,series_id):
    user_nickname = PlayerProfile.nickname
    
    #series_id = request.GET.get('series_id')
    #points = request.GET.get('additional_score')
    points=additional_score
    if not QuizSession.objects.filter(player=nickname, series_id=series_id).exists():
        # If it does not exist, a new record is created
        points = additional_score
        QuizSession.objects.create(
            series_id=series_id,
            player=nickname,
            score=points
        )
    if Activity.objects.get(series_id=series_id).status=='ended':
       #QuizSession.objects.filter(series_id=series_id).count() >= max_player:
        players = QuizSession.objects.filter(series_id=series_id).order_by('-score')
        players_list = list(players.values('player', 'score'))
        # Ranking and bonus points
        top_players = players[:3]
        for i,session in enumerate(top_players):
            PlayerProfile.objects.filter(nickname=nickname).update(score=F('score') + (3 - i))  # Hypothetical bonus logic
        # Clearing QuizSession
        QuizSession.objects.filter(series_id=series_id).delete()
        return render(request, 'quiz_leaderboard.html', {'players_list': players_list,'nickname':nickname})
    else:
        return render(request, 'waiting_page.html', {'series_id': series_id})
    
