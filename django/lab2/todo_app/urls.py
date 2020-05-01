from django.urls import path
from . import views

urlpatterns=[
    path("", views.todo_app, name = "todo_app"),
    path('createtasks', views.create_tasks, name="createTasks"),
    path('viewtasks', views.showTasks, name="viewTasks"),
    path('removetasks', views.remove_task, name= "remove"),
]



