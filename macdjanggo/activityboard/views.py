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

def scan_qr_code(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')
        if uploaded_file:
            # 读取上传的图片文件数据
            image_data = uploaded_file.read()
            # 使用 OpenCV 读取图像
            img = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)
            # 将图像转换为灰度图像
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # 使用 OpenCV 识别 QR Code
            detector = cv2.QRCodeDetector()
            retval, decoded_info, points, straight_qrcode = detector.detectAndDecodeMulti(gray)
            if retval:
                # 如果返回值是元组，则遍历处理每个 QR Code
                if isinstance(decoded_info, tuple):
                    for qr_code_url in decoded_info:
                        # 检查解析出的 URL 是否以 http:// 或 https:// 开头，如果不是，则添加相应的协议前缀
                        if not qr_code_url.startswith('http://') and not qr_code_url.startswith('https://'):
                            qr_code_url = 'http://' + qr_code_url
                        # 将 URL 转换为字符串，并进行重定向
                        return HttpResponseRedirect(str(qr_code_url))
                else:
                    # 如果返回值不是元组，则直接处理解析出的 URL
                    qr_code_url = decoded_info
                    # 检查解析出的 URL 是否以 http:// 或 https:// 开头，如果不是，则添加相应的协议前缀
                    if not qr_code_url.startswith('http://') and not qr_code_url.startswith('https://'):
                        qr_code_url = 'http://' + qr_code_url
                    # 将 URL 转换为字符串，并进行重定向
                    return HttpResponseRedirect(str(qr_code_url))
            else:
                return HttpResponseBadRequest('No QR Code found in uploaded image.')
        else:
            return HttpResponseBadRequest('No file uploaded.')
    else:
        return render(request, 'activity_join.html')