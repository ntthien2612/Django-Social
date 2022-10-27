from django.urls import path,include
from user.views import dashboard
from user.views import login1,register

urlpatterns = [
    path("",login1,name="login1"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", dashboard, name="dashboard"),
    path("register/", register, name="register"),
]