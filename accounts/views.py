from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
# Create your views here.
def register(request):
    form = UserCreationForm()
    if form.is_valid():
        user = form.save()
        login(request,user)
        messages.success(request,"Successfully registered and logged in !!")
    context ={
        "form":form,
    }
    return render(request,"register.html",context=context)