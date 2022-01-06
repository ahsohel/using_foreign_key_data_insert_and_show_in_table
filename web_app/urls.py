from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result_save/', views.result_save, name='result_save'),
    path('student_save/', views.student_save, name='student_save'),
    path('show_data_of_result', views.show_data_of_result, name='show_data_of_result'),
]