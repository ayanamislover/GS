from django.urls import path
from . import views

urlpatterns = [
    # 用于处理扫描QR码的视图
    path('check_location/', views.check_location, name='check_location'),
    path('scan/', views.scan_qr_code, name='scan_qr_code'),
    path('<str:qr_code>/', views.process_qr_code, name='process_qr_code'),

]
