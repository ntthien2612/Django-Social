from pyexpat.errors import messages
from unittest import result
from django.shortcuts import render,redirect

from .models import Comment, Post
from user.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import PostForm, UpdateForm
from django.shortcuts import (get_object_or_404, HttpResponseRedirect)

from django.http import JsonResponse
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
@login_required
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
"""  my post """
@login_required
def mypost(request): 
    post = Post.objects.filter(
        author=request.user
    )
    return render(
        request,
        "blog/mypost.html",{"blogs":post})

""" Edit my post """
@login_required
def editpost(request,id):
        post1 = Post.objects.get(pk=id)
        form = UpdateForm(request.POST or None, request.FILES, instance=post1)
        if form.is_valid():
             form.save()
             return redirect("/mypost")
        return render(request,"blog/editpost.html",{"post1": post1,"form": form})
""" Delete my post """
@login_required
def delete(request, id):
    blog = get_object_or_404(Post, pk=id) 
    blog.delete()
    return redirect('/mypost')

""" Search by post title or username """
@login_required
def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        posts = Post.objects.filter(title__contains=searched)
        return render(request, 'blog/search_results.html',{'searched':searched,'posts':posts})
    else:
        return render(request, 'blog/search_results.html',{})

""" like post """
@login_required
def likes(request):
    if request.method == "GET":
        post_like = request.GET.get('button_like')
        # action_like = request.GET.get('action_like')
        post = Post.objects.get(pk = post_like)
        

        try:
            check_like = post.likes.get( pk=request.user.profile.pk)
        except:
            check_like = ''

        if check_like != '' :
            print("xoa like", check_like)
            post.likes.remove(request.user)
        else:
            print("like")
            post.likes.add(request.user)
        
        count_like = post.likes.count()
        print(count_like)

    return JsonResponse({"valid":"tao ne", "post_like" : count_like }, status = 200)