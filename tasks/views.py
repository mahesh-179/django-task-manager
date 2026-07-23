from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from django.contrib import messages
from .models import Task,Profile
from .forms import ProfileCreate
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
            user=request.user,
            task_name=task_name,
            category=category,
            priority=priority,
            is_completed=is_completed,
        )
        messages.success(request,"Successfully created a task")
        return redirect("home")
    return render(request,"create.html")



    



def profile_pic(request):
        has_profile = Profile.objects.filter(user=request.user).exists()
        if has_profile:
             profile = Profile.objects.get(user=request.user)
             return redirect("profile", profile.id)
        if request.method == "POST":
            form = ProfileCreate(request.POST,request.FILES)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                messages.success(request,"Profile Updated Successfully")
                return redirect("profile",profile.id)
        else:
            form = ProfileCreate()
        context = {
            "form":form,
            "has_profile":has_profile,
        }
        return render(request,"create_profiles.html",context=context)

def profile_display(request,id):
    has_profile = Profile.objects.filter(user=request.user).exists()
    profile = get_object_or_404(Profile,id=id)
    context = {
        "profile":profile,
        "has_profile":has_profile,
    }
    return render(request,"display_profile.html",context=context)


def update_task(request,id):
    task = get_object_or_404(Task,id=id)
    if request.method=="POST":
        task.task_name = request.POST.get('task_name')
        task.category = request.POST.get('category')
        task.priority = request.POST.get('priority')
        task.is_completed="is_completed" in request.POST
        task.save()
        return redirect("home")
    context ={
        "task":task,
    }
    return render(request,"update.html",context=context)


