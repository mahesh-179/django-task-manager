from django.shortcuts import render,redirect
from .models import Task
from django.contrib import messages
from .models import Task
# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect("welcome")
    else:
        tasks = Task.objects.filter(user=request.user)
        context={
            "tasks":tasks,
        }
    return render(request,"home.html",context=context)
def welcome(request):
    return render(request,"welcome.html")
def change_status(request,id):
    if request.method=="POST":
        task = Task.objects.get(id=id)
        task.is_completed = True
        task.save()
        messages.success(request,"You have completed a task!!!")
    return redirect('home')

def create_task(request):
    if request.method=='POST':
        task_name = request.POST.get('task_name')
        category = request.POST.get('category')
        priority = request.POST.get('priority')
        is_completed="is_completed" in request.POST
        Task.objects.create(
            user=request,
            task_name=task_name,
            category=category,
            priority=priority,
            is_completed=is_completed,
        )
        messages.success(request,"Successfully created a task")
        return redirect("home")
    return render(request,"create.html")



    
def update_task(request):
    return render(request,"update.html")


