
from django.urls import path

from . import views

urlpatterns = [
    path('', views.TaskFormView.as_view(), name="home"),
    path('show_task/', views.TaskListView.as_view(), name="show_task"),
    path('edit_task/<int:pk>', views.TaskUpdateView.as_view(), name="edit_task"),
    path('delete_task/<int:pk>', views.TaskDeleteView.as_view(), name="delete_task"),
    path('complete_task/<int:pk>', views.CompleteTaskView.as_view(), name="comp_task"),
    path('completed_tasks/', views.TaskCompletedListView.as_view(), name="completed_task"),
]