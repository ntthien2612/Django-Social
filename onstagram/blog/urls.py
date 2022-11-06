from django.urls import path
from . import views
from .views import  dashboard,newpost,mypost,delete,search,likes
urlpatterns = [
    path('indexdashboard/',dashboard, name='indexdashboard'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('post/',newpost, name='postnew'),
    path('mypost/',mypost, name='mypost'),
    path('delete/<str:id>/', delete, name="delete"),
    path('search/',search, name='search'),
    path('home/likes/', views.likes, name='likes'),
]