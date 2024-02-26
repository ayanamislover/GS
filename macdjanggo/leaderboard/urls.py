from django.urls import path
from leaderboard import views
urlpatterns = [
    path('', views.user_leaderboard, name='user_leaderboard'),
]
