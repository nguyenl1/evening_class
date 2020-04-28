from django.shortcuts import render
from .models import Tasks 

# Create your views here.

def todo_app(request):
    return render(request, "index.html")

def index(request):
    tasks1 = Tasks(tasks = 'fold my clothes')
    tasks2 = Tasks(tasks = 'wash the car')
    tasks3 = Tasks(tasks= 'bathe the dogs')

    tasks1.save()
    tasks2.save()
    tasks3.save()

    return render(request,'index.html')

def showTasks(request):
    tasks = Tasks.objects.all()
    print(tasks)

    context = {
        'tasks':tasks, 
    }

    return render(request,'tasks.html', context=context)
