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

def show_tasks(request):
    tasks = Task.objects.all()

    context = {
        'tasks':tasks, 
    }

    return render(request,'view_tasks.html', context=context)

# def create_tasks(request):
#     if request.method == 'POST':
#         if request.POST.get('task_name') and request.POST.get('due_date') and request.POST.get('is_completed'):
        
        

#             create_task = Task()
#             create_task.task_name = request.POST.get('task_name')
#             create_task.due_date = request.POST.get('due_date')
#             create_task.is_completed = request.POST.get('is_completed')
#             create_task.save()

#             return render(request, "create_task.html")
#     else:
#         return HttpResponse('invalid method')

def create_tasks(request):
    return render(request, "create_task.html")


def remove_tasks(request,id):
    return render(request, "remove_tasks.html")

def completed(request):
    pass 

def show_details(request,id):
    desp = Task.objects.get(pk=id)

    context = {
        'desp':desp,
    }

    return render(request, "show_details.html", context=context)


