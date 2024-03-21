from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout_view, name='logout_view'),    
    path('login/', views.login, name='login'),
    path('regist/', views.regist, name='regist'),
    path('gdpr/',views.gdpr,name='gdpr'),
    path('', views.index, name='index'),
]
