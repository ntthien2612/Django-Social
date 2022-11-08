from django.shortcuts import render,redirect
from django.urls import reverse
from user.forms import CustomUserCreationForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Profile
from blog.models import Post

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


def profile(request, pk):
    if(request.method == 'GET'):
        profile = Profile.objects.get(pk=pk)
        profile.following.add(profile)

        iduser = str(request.user.profile.pk)
        idlink = str(pk)

        post = Post.objects.filter(
        author=request.user
        )
       
        return render(request, "users/profile.html",{"profile": profile,'iduser': iduser,'idlink': idlink,'blogs':post})

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
       
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect('/profile/'+str(pk))
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

   
def follows (request,pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("following")
        if action == "follow":
            current_user_profile.following.add(profile)
        elif action == "unfollow":
            current_user_profile.following.remove(profile)
        current_user_profile.save()   
    return redirect('/profile/'+str(pk))

def follower(request):
     profile = Profile.objects.get(pk=request.user.profile.pk) 
     return render(
        request ,
        "users/follower.html",{"profile":profile})

def follow(request):
     profile = Profile.objects.get(pk=request.user.profile.pk)
     return render(
        request ,
        "users/follows.html",{"profile":profile})