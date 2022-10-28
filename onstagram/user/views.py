from django.shortcuts import render,redirect
from django.urls import reverse
from user.forms import CustomUserCreationForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Profile

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

# def profile1(request):
#     print(request)
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
        
#         p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
       
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f"Your account has been updated!")
#             return redirect('/profile/')
#     else:
#         print ("anhduy")
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
    
#     context = {
#         'u_form':u_form,
#         'p_form':p_form
#     }

#     return render(request, 'users/profile.html', context)

def profile(request, pk):
    if(request.method == 'GET'):
        profile = Profile.objects.get(pk=pk)
        

        return render(request, "users/profile.html", {"profile": profile})

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

   
   