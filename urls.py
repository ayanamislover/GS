from django.urls import path
from signin import compare_location
from scan_qrcode import check_in
urlpatterns = [
    path('compare_location/', compare_location, name='compare_location'),
]
urlpatterns = [
    path('check-in/', check_in, name='check-in'),
]