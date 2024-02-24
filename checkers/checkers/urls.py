from django.contrib import admin
from django.urls import path
from navi.views import map_view  # 修改这里

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map_view/', map_view, name='map_view'),
]
