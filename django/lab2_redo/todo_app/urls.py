from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name = "home"),
    path('createtask', views.create_task, name="create_task"),
    path('taskdetails', views.task_details, name="task_details"),
    path('removetask', views.remove_task, name="remove_task"),

]