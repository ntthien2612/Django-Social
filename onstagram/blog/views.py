from django.shortcuts import render
from .models import Comment, Post 
from django.contrib.auth.decorators import login_required

""" Home page with all posts """


def home(request):
    
    return render(
        request ,
        "blog/home.html",)

def dashboard(request):
    
    return render(
        request ,
        "blog/first.html",)
@login_required
def about(request):
    
    return render(
        request ,
        "blog/about.html",)