from django.shortcuts import render
from .models import TodoItem


def home(request):
    return render(request, "index.html")

def create_task(request):
    return render(request, "create_task.html")

def task_details(request):
    return render(request, "task_details.html")

def remove_task(request):
    return render(request, "remove_task.html")

