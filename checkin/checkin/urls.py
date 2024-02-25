from django.contrib import admin
from django.urls import path, include  # 确保导入了include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('scan2checkin/', include('scan2checkin.urls'))
]
