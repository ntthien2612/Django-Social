from unittest import result
from django.shortcuts import render

from .models import Comment, Post
from user.models import Profile
from django.contrib.auth.decorators import login_required

""" Home page with all posts """

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