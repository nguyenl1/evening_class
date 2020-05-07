from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def home(request):
    list_tasks = TodoItem.objects.all()

    context = {
        'tasks':list_tasks,
    }
    
    return render(request, "index.html", context=context)

def task_details(request, id):
    desp = TodoItem.objects.get(pk=id)

    context = {
        'desp':desp,
    }

    return render(request, "task_details.html", context=context)

def remove_task(request,id):
    task = get_object_or_404(TodoItem, pk=id)
    task.delete()
    return redirect("home")

def edit_task(request,id):
    task = TodoItem.objects.get(pk=id)

    context = {
        'task': task
    }
    return render(request,"edit_task.html", context=context)


def update_task(request,id):
    

    task = TodoItem.objects.get(pk=id)

    if request.POST.get('is_completed', False) == "on":
        task.task_name = request.POST['task_name']
        task.complete_task()
        task.save()


    return redirect('home')


def create_task(request):

       #https://stackoverflow.com/questions/57288652/save-html-form-data-in-database-django?rq=1

    if request.method == 'POST':
        
        task_name = request.POST['task_name']
        due_date = request.POST['due_date']
        

        TodoItem.objects.create(task_name=task_name, due_date=due_date, )

        

        return redirect('create_task')
    else:
        return render(request,'create_task.html')
