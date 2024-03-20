from django.urls import path
from . import views

urlpatterns = [
    # ...
    path("list/", views.list, name='list'),
    path("<str:title>/",views.detail,name='detail'),
]