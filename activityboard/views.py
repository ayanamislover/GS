import cv2
from django.urls import reverse
import numpy as np
import base64
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseBadRequest, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from io import BytesIO
import qrcode
from django.db.models import F
from activityboard.models import  QuizSession
from aM.models import Activity
from usersinformation.models import PlayerProfile
from answerquestion.models import Series
# Create your views here.



def activity_join(request):
    return render(request, 'activity_join.html')

def generate_qrcode(request):
    series_id=1
    # 创建一个 QR Code 对象
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # 设置要编码的数据（这里可以是任何你想要在 QR Code 中包含的信息）
    targeturl=reverse('enternickname',kwargs={'series_id':1})
    qr.add_data(targeturl)  # 这里替换成你的答题页面 URL
    qr.make(fit=True)
    # 创建一个图像对象并将 QR Code 渲染到图像中
    img = qr.make_image(fill_color="black", back_color="white")
    # 将图像保存到 BytesIO 对象中
    buffer = BytesIO()
    img.save(buffer)
    # 将图像返回给客户端
    return HttpResponse(buffer.getvalue(), content_type="image/png")

def enternickname(request,series_id):
    series = get_object_or_404(Series, pk=series_id)
    if request.method == "POST":
        nickname = request.POST.get("nickname")
        if PlayerProfile.objects.filter(nickname=nickname).exists():
            # 如果nickname存在，重定向到目标URL
            target_url_name=reverse('ans:series_detail',kwargs={'series_id': 1, 'nickname': nickname})
            return redirect(target_url_name)  # 确保替换 "target_url_name" 为你的目标URL的name
        else:
            # 如果nickname不存在，可以选择显示错误消息或者其他操作
            return render(request, "enternickname.html", {"error": "Nickname not found."})
    else:
        # 如果是GET请求，显示输入表单
        return render(request,'enternickname.html')

def scan_qr(request):
    return render(request, 'scan_qr.html')

def quiz_leaderboard(request,nickname,additional_score,series_id):
    user_nickname = PlayerProfile.nickname
    
    #series_id = request.GET.get('series_id')
    #points = request.GET.get('additional_score')
    points=additional_score
    QuizSession.objects.create(
    series_id=series_id,
    player=nickname,
    score=points
    )
    # 检查是否达到max_player
    max_player = Activity.objects.first().max_participants
    if Activity.objects.get(pk=series_id).status=='ended':
       #QuizSession.objects.filter(series_id=series_id).count() >= max_player:
        players = QuizSession.objects.filter(series_id=series_id).order_by('-score')
        players_list = list(players.values('player', 'score'))
        # 排名和加分
        top_players = players[:3]
        for i,session in enumerate(top_players):
            PlayerProfile.objects.filter(nickname=nickname).update(score=F('score') + (3 - i))  # 假设加分逻辑
        # 清空QuizSession
            
        QuizSession.objects.filter(series_id=series_id).delete()
        return render(request, 'quiz_leaderboard.html', {'players_list': players_list,'nickname':nickname})
    else:
        return render(request, 'waiting_page.html', {'series_id': series_id})