from django.shortcuts import render
from django.utils import timezone
from .models import Task 
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


# Create your views here.



def todo_app(request):
    tasks = Task.objects.all()

    context = {
        'tasks':tasks,
    }

    return render(request, "index.html", context=context)

def showTasks(request):
    tasks = Task.objects.all()

    context = {
        'tasks':tasks, 
    }

    return render(request,'view_tasks.html', context=context)

def create_tasks(request):
    # if request.method == 'POST':
    #     data = request.POST
    #     Task.objects.create(
    #         task_name = data['task_name'],
    #         due_date = data['due_date'],
    #         is_completed = data['is_completed']
    #     )

    #     task_name.save()
    #     due_date.save()
    #     is_completed()

        return render(request, "create_task.html")
    # else:
    #     return HttpResponse('invalid method')

def remove_task(request):
    return render(request, "remove_tasks.html")

def completed(request):
    pass 


