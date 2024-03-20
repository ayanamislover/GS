from django.urls import path
from . import views

urlpatterns = [
    path('<str:nickname>', views.checkersgame, name='checkers_game'),
    path('check_location/<str:nickname>/<str:tag>', views.check_location, name='check_location'),
    path('cal_carbon/<str:nickname>', views.cal_carbon, name='cal_carbon'),
]
