from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request,"Password doesn't match please write correctly !")
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists with this")
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already exists with this")
            return redirect('register')

        user=User.objects.create_user(
            username=username,
            email=email,
            password=password1,
        )
        messages.success(request, "Account created successfully.")
        login(request,user)
        return redirect("home")
    return render(request,"register.html")

from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in!")
            return redirect("home")
        else:
            messages.error(request, "Incorrect username or password.")

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("login")