# pointshop/urls.py
from django.urls import path
from .views import shop, lottery_draw, buy_product, product_detail
from .views import search_results
urlpatterns = [
    path('<str:nickname>/', shop, name='shop'),  
    path('search/', search_results, name='search_results'),
    path('lottery/draw/', lottery_draw, name='lottery_draw'),  # lottery URL
    path('buy/<str:name>/<str:nickname>/', buy_product, name='buy_product'),
    path('product/<str:name>/<str:nickname>/', product_detail, name='product_detail'),

]

