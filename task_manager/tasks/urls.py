from django.urls import path
from . import views

urlpatterns = [
    path('task-list/', views.task_list, name='task-list'),  # 👈 Add this
    path('create/', views.create_task, name='create-task'),
    path('update/<int:pk>/', views.update_task, name='update-task'),
    path('delete/<int:pk>/', views.delete_task, name='delete-task'),
]
