from django.shortcuts import render,redirect
from .models import Task
# Create your views here.
def home(request):
    tasks = Task.objects.all().order_by('id')
    context={
        "tasks":tasks,
    }
    return render(request,"home.html",context=context)

def change_status(request,id):
    if request.method=="POST":
        task = Task.objects.get(id=id)
        task.is_completed = True
        task.save()
    return redirect('home')