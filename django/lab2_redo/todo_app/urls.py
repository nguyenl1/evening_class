from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name = "home"),
    path('createtask', views.create_task, name="create_task"),
    path('taskdetails/<int:id>', views.task_details, name="task_details"),
    path('removetask/<int:id>', views.remove_task, name="remove_task"),
    path('edittask/<int:id>', views.edit_task, name="edit_task"),
    path('updatetask/<int:id>', views.update_task, name="update_task"),

]