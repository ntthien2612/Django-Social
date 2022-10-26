from django.shortcuts import render,redirect
from django.urls import reverse
from user.forms import CustomUserCreationForm
from django.contrib.auth import login

def dashboard(request):
    return render(request, "users/dashboard.html")

def login1(request):
    response = redirect('accounts/login/')
    return response

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("http://localhost:8000/accounts/login/")