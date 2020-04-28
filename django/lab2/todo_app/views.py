from django.shortcuts import render
from .models import Task 

# Create your views here.

def todo_app(request):
    return render(request, "index.html")

def index(request):
    task1 = Task(task = 'fold my clothes')
    task2 = Task(task = 'wash the car')
    task3 = Task(task= 'bathe the dogs')

    task1.save()
    task2.save()
    task3.save()

    return render(request,'index.html')

def showTasks(request):
    tasks = Task.objects.all()

    context = {
        'tasks':tasks, 
    }

    return render(request,'tasks.html', context=context)
