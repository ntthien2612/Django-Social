from django.urls import path,include
from user.views import dashboard
from user.views import login1,register,profile,follows,follower,follow

urlpatterns = [
    path("",login1,name="login1"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", dashboard, name="dashboard"),
    path("register/", register, name="register"),
    path("profile/<int:pk>",profile,name="profile"),
    path("follows/<int:pk>",follows,name="follows"),
    path("follower/",follower),
    path("follows/",follow)
    
]