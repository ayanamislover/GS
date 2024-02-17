from django.urls import path

from . import views

urlpatterns = [

    path("<str:nickname>/", views.detail, name="detail"),
    path("", views.player_profile, name="player_profile"),
]