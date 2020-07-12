from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('questions/', views.index_question, name='index'),
    path('questions/<int:question_id>', views.detail, name='detail'),
]
