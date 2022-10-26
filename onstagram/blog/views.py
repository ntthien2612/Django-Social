from django.shortcuts import render
from .models import Comment, Post 
""" Home page with all posts """

def dashboard(request):
    
    return render(
        request ,
        "first.html",)

def about(request):
    
    return render(
        request ,
        "about.html",)