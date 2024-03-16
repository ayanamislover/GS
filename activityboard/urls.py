from django.urls import path
from . import views

urlpatterns = [
    path('', views.activity_join, name='activity_join'),
    path('activity/leaderboard/<str:nickname>/<int:additional_score>/<int:series_id>/',views.quiz_leaderboard,name='quiz_leaderboard'),
    #path('activity/leaderboard/<str:nickname>/',views.quiz_leaderboard,name='quiz_leaderboard'),
    path('activity/qrcode/<int:series_id>/',views.generate_qrcode,name='qrcode'),
    path("activity/scanqrcode/",views.scan_qr, name='scan_qr'),
    path("activity/enternickname/<int:series_id>",views.enternickname,name="enternickname"),
]