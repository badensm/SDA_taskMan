from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>/', views.detail_task, name='detail_task'),
    path('tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('tasks/<int:task_id>/complete/', views.complete_task, name='complete_task'),

]
