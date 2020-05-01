from django.urls import path
from . import views

urlpatterns=[
    path("", views.todo_app, name = "todo_app"),
    # path('mytasks', views.showTasks, name="showTasks"),
    path('createtasks', views.create_tasks, name="createTasks"),
    path('task/<int:pk>/', views.task_detail, name ='tasks_detail'),
    path('viewtasks', views.list_tasks, name="viewTasks"),
    path('removetasks', views.remove_task, name= "remove"),
]



