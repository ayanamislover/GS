from django.urls import path
from . import views

# path('', views.index, name='index')定义了应用的根URL到index视图的映射。这个视图将显示可用的题目列表。
#path('questions/<int:question_id>/', views.detail, name='detail')定义了一个动态URL，用于显示每个题目的详情页。<int:question_id>部分是一个路径转换器，它捕获URL中的数字并将其作为question_id参数传递给detail视图函数。
#path('submit_answer/<int:question_id>/', views.submit_answer, name='submit_answer')是用于处理答案提交的URL。同样，它将题目的ID作为参数传递给submit_answer视图函数。

urlpatterns = [
    path('', views.index, name='index'),  # 主页/题目列表
    path('questions/<int:question_id>/', views.detail, name='detail'),  # 题目详情页
    path('submit_answer/<int:question_id>/', views.submit_answer, name='submit_answer'),  # 提交答案的处理
]
