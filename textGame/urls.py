from django.urls import path
from . import views
app_name='textGame'

urlpatterns=[
    path('meadow/<str:nickname>/', views.MeadowAd, name='MeadowAd'),
    path('SceneSelect/<int:loc_id>/<str:nickname>/', views.SceneSelect, name='SceneSelect'),
]
