# rewards/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.gift_list, name='gift_list'),
    path('detail/<int:id>/', views.gift_detail, name='gift_detail'),
]
