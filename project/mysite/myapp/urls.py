from django.urls import path

from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('questions/', views.index_question, name='question_list'),
    path('questions/<int:question_id>', views.detail, name='question_detail'),
]
