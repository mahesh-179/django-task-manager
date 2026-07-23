from django.shortcuts import render,redirect
from .models import Task
from django.contrib import messages
# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect("welcome")
    else:
        tasks = Task.objects.all().order_by('id')
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



