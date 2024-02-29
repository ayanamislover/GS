from django.urls import path
from . import views

app_name = 'ans'

urlpatterns = [
    path('', views.index_none, name='index_none'),  # main
    path('<str:nickname>/', views.index, name='index'),  # get nickname in url
    path('submit_answers/<int:question_id>/', views.submit_answers, name='submit_answers'),
    path('series/<int:series_id>/<str:nickname>/', views.series_detail, name='series_detail'),
    path('results_page/<str:nickname>/<int:series_id>/', views.results_page, name='results_page'),  # result page url
]
