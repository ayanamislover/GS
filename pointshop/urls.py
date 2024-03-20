# pointshop/urls.py
from django.urls import path
from .views import shop, lottery_draw, buy_product, product_detail
from .views import search_results
urlpatterns = [
    path('<str:nickname>/', shop, name='shop'),  # 确保这个URL模式指向了上面创建的视图函数
    path('search/', search_results, name='search_results'),
    path('lottery/draw/', lottery_draw, name='lottery_draw'),  # 抽奖URL
    path('buy/<str:name>/<str:nickname>/', buy_product, name='buy_product'),
    path('product/<str:name>/<str:nickname>/', product_detail, name='product_detail'),

]

