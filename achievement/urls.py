from django.urls import path

from . import views

urlpatterns = [
    #Main view
    path("", views.achievement_detail, name="ahchievement_detail"),

]