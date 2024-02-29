from django.urls import path
from . import views

urlpatterns = [
    path('game/<str:nickname>', views.checkersgame, name='checkers_game'),
    path('check_location/<str:nickname>', views.check_location, name='check_location'),
]
