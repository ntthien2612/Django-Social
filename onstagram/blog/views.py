from unittest import result
from django.shortcuts import render,redirect

from .models import Comment, Post
from user.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import PostForm
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

    profile = Profile.objects.get(pk=request.user.profile.pk) 
    f=profile.following.all() 
    profiles= Profile.objects.all().exclude(follow_by__in=f)
    return render(
        request ,
        "blog/about.html",{"profile":profiles})

def newpost(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES or None)
        print(request.FILES)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.author = request.user
            dweet.save()
            return redirect("home")
    form = PostForm()
    return render(request, "blog/newpost.html", {"form": form})