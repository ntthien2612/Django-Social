from unittest import result
from django.shortcuts import render,redirect

from .models import Comment, Post
from user.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import PostForm
from django.shortcuts import (get_object_or_404, HttpResponseRedirect)

""" Home page with all posts """

@login_required
def home(request):
    
    followed_posts = Post.objects.filter(
        author__profile__in=request.user.profile.following.all()
    ).order_by("-date_posted")
    return render(request,"blog/home.html",{"blogs": followed_posts})

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
    form = PostForm(request.POST, request.FILES or None)
    if request.method == "POST":
        print(request.FILES)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.author = request.user
            dweet.save()
            return redirect("/home")
    return render(request,"blog/newpost.html",{"form": form})

def mypost(request): 
    post = Post.objects.filter(
        author=request.user.profile.pk
    )
    return render(
        request,
        "blog/mypost.html",{"blogs":post})

""" Delete my post """
def delete(request, id):
    blog = get_object_or_404(Post, id=id) 
    blog.delete()
    return redirect('/mypost')

""" Search by post title or username """
def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        posts = Post.objects.filter(title__contains=searched)
        return render(request, 'blog/search_results.html',{'searched':searched,'posts':posts})
    else:
        return render(request, 'blog/search_results.html',{})