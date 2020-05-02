from django.urls import path
from . import views

urlpatterns=[
    path("", views.todo_app, name = "todo_app"),
    path('createtasks', views.create_tasks, name="createTasks"),
    path('showtasks', views.show_tasks, name="showTasks"),
    path('removetasks', views.remove_tasks, name= "removeTasks"),
    path('showdetails/<int:id>', views.show_details, name = "showDetails"),
]



