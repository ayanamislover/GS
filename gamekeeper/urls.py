from django.urls import path
from gamekeeper import views
urlpatterns = [
    path('',views.user_login,name='gamekeeperlogin'),
    path('homepage/', views.gamekeeper, name='gamekeeper'),
    path('changestatue/', views.change_status, name='changestatue'),
    path('generateqrcodebyseries/',views.gamekeeper_qrcode,name='generateqrcodebyid'),
    path('review_photos/', views.review_photos, name='review_photos'),
]
