from django.urls import path
from . import views
from .views import  dashboard
urlpatterns = [
    path('', views.dashboard, name='indexdashboard'),
    path('about/', views.about, name='about'),
]