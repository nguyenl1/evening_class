from django.urls import path
from . import views

urlpatterns=[
    path("", views.todo_app, name = "todo_app"),
    path('mytasks', views.showTasks, name="showTasks"),
]

