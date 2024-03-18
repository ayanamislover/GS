from django.urls import path
from . import views

urlpatterns=[
    path('meadow/<str:nickname>/', views.MeadowAd, name='MeadowAd'),
]
