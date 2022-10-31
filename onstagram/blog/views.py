from django.shortcuts import render
from .models import Comment, Post 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
""" Home page with all posts """

@login_required
def home(request):
    
    posts = Post.objects.all()
    return render(
        request,
        "blog/home.html",
        {"blogs": posts}
    )

@login_required
def dashboard(request):
    
    return render(
        request ,
        "blog/first.html",)
@login_required
def about(request):
    return render(request, 'blog/about.html', {'title':'About'})


