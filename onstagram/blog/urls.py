from django.urls import path
from . import views
from .views import  dashboard,newpost
urlpatterns = [
    path('indexdashboard/', views.dashboard, name='indexdashboard'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('post/',newpost, name='postnew')
]