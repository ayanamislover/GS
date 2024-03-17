from django.urls import path
from pictures import views
from django.views.generic import RedirectView
from django.conf.urls.static import static

urlpatterns = [
    path('<str:nickname>/', views.upload_view, name='upload_view'),  # 对应 photo 视图
    path("api/upload", views.upload_api, name='upload_api'),
]
