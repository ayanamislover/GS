from django.urls import path
from . import views

app_name = 'ans'
# path('', views.index, name='index')定义了应用的根URL到index视图的映射。这个视图将显示可用的题目列表。
#path('questions/<int:question_id>/', views.detail, name='detail')定义了一个动态URL，用于显示每个题目的详情页。<int:question_id>部分是一个路径转换器，它捕获URL中的数字并将其作为question_id参数传递给detail视图函数。
#path('submit_answer/<int:question_id>/', views.submit_answer, name='submit_answer')是用于处理答案提交的URL。同样，它将题目的ID作为参数传递给submit_answer视图函数。

urlpatterns = [
    path('', views.index_none, name='index_none'),  # 主页/题目列表
    path('<str:nickname>/', views.index, name='index'),  # 假设你希望URL路径包含用户ID
    path('submit_answers/<int:question_id>/', views.submit_answers, name='submit_answers'),  # 提交答案的处理
    path('series/<int:series_id>/<str:nickname>/', views.series_detail, name='series_detail'),
    path('results_page/<str:nickname>/', views.results_page, name='results_page'),  # 假设你有一个结果视图
]
