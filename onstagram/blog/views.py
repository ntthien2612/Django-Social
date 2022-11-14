from pyexpat.errors import messages
from unittest import result
from django.shortcuts import render,redirect,get_object_or_404

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
    profile = Profile.objects.get(pk=request.user.profile.pk)
    
    profile.following.add(profile)
    print(profile.following.add(profile))
    followed_posts = Post.objects.filter(
        author__profile__in=request.user.profile.following.all()
    ).order_by("-date_posted")

    profile = Profile.objects.get(pk=request.user.profile.pk)

    post1 = Post.objects.filter(likes = request.user)

    mypost = Post.objects.filter(
        author=request.user
    )

    comment_post = Comment.objects.all().order_by("date_added")
    


    
    return render(request,"blog/home.html",{"blogs": followed_posts,"profile":profile,"post":post1,"mypost":mypost, "comment_post" : comment_post})

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
    print(post)

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
             return redirect("/home")
        return render(request,"blog/editpost.html",{"post1": post1,"form": form})
""" Delete my post """
@login_required
def delete(request, id):
    blog = get_object_or_404(Post, pk=id) 
    blog.delete()
    user = request.user.profile.pk
    return redirect('/profile/'+str(user))

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
        check_like = ''

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

@login_required
def comment(request):
    if request.method == "GET":
        comment_body = request.GET.get('comment_body')
        post_id = request.GET.get('post_id')
        post = Post.objects.get(pk = post_id)
        print(post_id)
        print(comment_body)

        cmt = Comment.objects.create(post = post, name = request.user, body = comment_body )

        comment_post = Comment.objects.get(pk = cmt.pk)
        comment_time = comment_post.date_added
        comment_user = comment_post.name.username
        # user_image = cmt.name.profile.image
    return JsonResponse({ "comment_post": comment_post.body , "comment_time": comment_time, "comment_user": comment_user  }, status = 200)