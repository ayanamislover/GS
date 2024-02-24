from django.urls import path
from signin import compare_location
from scan_qrcode import check_in
from django.urls import path
from . import checkin_views  # 导入 checkin_views 模块

urlpatterns = [
    path('compare-location/', checkin_views.compare_location, name='compare_location'),
]

urlpatterns = [
    path('compare_location/', compare_location, name='compare_location'),
]
urlpatterns = [
    path('check-in/', check_in, name='check-in'),
]


