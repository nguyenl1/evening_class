from django.shortcuts import render
from django.utils import timezone
from .models import Task 
from django.http import HttpResponse

# Create your views here.

def todo_app(request):
    return render(request, "index.html", {})

def create_tasks(request):
    if request.method == 'POST':
        data = request.POST
        Task.objects.create(
            task_name = data['task_name'],
            desp = data['desp'],
            due_date = data['due_date']

        )

        return redirect('todo_app')
    else:
        return HttpResponse('invalid method')


def task_detail(request,pk):
    task = get_list_or_404(Task, pk=pk)
    return render(request,'view_tasks.html', {'post':post})

def remove_task(request):
    return render(request, "remove_tasks.html")

def list_tasks(request):
    return render(request, "view_tasks.html")

def completed(request):
    pass 

def showTasks(request):
    tasks = Task.objects.all()

    context = {
        'tasks':tasks, 
    }

    return render(request,'index.html', context=context)
