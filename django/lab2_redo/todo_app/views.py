from django.shortcuts import render, redirect
from .models import TodoItem
from django.http import HttpResponse


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

def remove_task(request):
    list_tasks = TodoItem.objects.all()

    context = {
        'tasks':list_tasks,
    }
    return render(request, "remove_task.html", context=context)




def create_task(request):

       #https://stackoverflow.com/questions/57288652/save-html-form-data-in-database-django?rq=1

    if request.method == 'POST':
        
        task_name = request.POST['task_name']
        due_date = request.POST['due_date']
        
        is_completed = request.POST.get['is_completed']
        if not is_completed:
            is_completed = True
        toSave = models.TodoItem(is_completed = is_completed)
        toSave.save()
        

        sub = TodoItem.objects.create(task_name=task_name, due_date=due_date, )

        return redirect('create_task')
    else:
        return render(request,'create_task.html')


    

    # if request.method=='POST': 
    #     if request.POST.get('task_name') and request.POST.get('due_date') and request.POST.get('is_completed'):
    #         create_task=TodoItem()
    #         create_task.task_name=request.POST.get('task_name')
    #         create_task.due_date=request.POST.get('due_date')
    #         create_task.is_completed=request.POST.get('is_completed')
    #         create_task.save()

    #         return render(request, "create_task.html")
    # else:
    #     return HttpResponse('invalid method')

    # if request.method == 'POST':
    #     data = request.POST

    #     taskText = data['taskText']
    #     is_completed = False

    #     new_task = TodoItem()
    #     new_task.task_name = taskText
    #     new_task.save()

    #     return redirect('home')
    # elif request.method == 'GET':
    #     return render(request,'create_task.html')
    # else:
    #     return HttpResponse('invalid method')

    # if request.method == 'POST':
    #     data = request.POST

    #     TodoItem.objects.create(
    #         task_name = data['task_name'],
    #         due_date = data['due_date'],
    #         is_completed = data ['is_completed'],
    #     )

    #     task_name.save()
    #     due_date.save()
    #     is_completed()

    #     return redirect('create_task')
    # else:
    #     return HttpResponse('invalid method')


 



        

