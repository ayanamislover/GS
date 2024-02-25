import cv2
import numpy as np
import base64
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseBadRequest, HttpResponse
from django.shortcuts import render, redirect
from io import BytesIO
import qrcode


# Create your views here.

def quiz_home(request):
    return render(request, 'quiz.html')

def activity_join(request):
    return render(request, 'activity_join.html')

def generate_qrcode(request):
    # 创建一个 QR Code 对象
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # 设置要编码的数据（这里可以是任何你想要在 QR Code 中包含的信息）
    qr.add_data('http://127.0.0.1:8000/activityboard/activity/quiz/')  # 这里替换成你的答题页面 URL
    qr.make(fit=True)
    # 创建一个图像对象并将 QR Code 渲染到图像中
    img = qr.make_image(fill_color="black", back_color="white")
    # 将图像保存到 BytesIO 对象中
    buffer = BytesIO()
    img.save(buffer)
    # 将图像返回给客户端
    return HttpResponse(buffer.getvalue(), content_type="image/png")


    
def scan_qr(request):
    return render(request, 'scan_qr.html')