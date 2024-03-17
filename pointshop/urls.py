# pointshop/urls.py
from django.urls import path
from .views import index, lottery_draw
from .views import search_results
urlpatterns = [
    path('', index, name='index'),  # 确保这个URL模式指向了上面创建的视图函数
    path('search/', search_results, name='search_results'),
    path('lottery/draw/', lottery_draw, name='lottery_draw'),  # 抽奖URL

]
