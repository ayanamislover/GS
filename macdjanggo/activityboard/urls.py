from django.urls import path
from . import views

urlpatterns = [
    #path('', views.activity_join, name='activity_join'),
    path('',views.scan_qr_code,name='scan_qr_code'),
    path('activity/quiz/', views.quiz_home, name='quiz_home'),
    path('activity/qrcode/',views.generate_qrcode,name='qrcode'),
    
]