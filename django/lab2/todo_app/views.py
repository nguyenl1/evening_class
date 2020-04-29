from django.shortcuts import render
from .models import Task 

# Create your views here.

def todo_app(request):
    return render(request, "index.html")

def index(request):
    task1 = Task(task_name = 'laundry', desp = 'fold my clothes', due_date = ' ')
    task2 = Task(task_name = 'car', desp = 'wash the car', due_date = ' ')
    task3 = Task(task_name = 'doggos', desp = 'bathe the dogs', due_date = ' ')

    task1.save()
    task2.save()
    task3.save()

    return render(request,'create_task.html')

def showTasks(request):
    tasks = Task.objects.all()

    context = {
        'tasks':tasks, 
    }

    return render(request,'index.html', context=context)
