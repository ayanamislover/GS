from django.urls import path
from . import views

urlpatterns = [
    path('game/', views.checkersgame, name='checkers game'),
    path('check_location/', views.check_location, name='check_location'),
]
