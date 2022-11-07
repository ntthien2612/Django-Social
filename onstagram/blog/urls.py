from django.urls import path
from . import views
<<<<<<< HEAD
from .views import  dashboard,newpost,mypost,delete,search,editpost
=======
from .views import  dashboard,newpost,mypost,delete,search,likes
>>>>>>> 10a7762507eab300f2f422ddf3cb4c14ad874dc2
urlpatterns = [
    path('indexdashboard/',dashboard, name='indexdashboard'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('post/',newpost, name='postnew'),
    path('mypost/',mypost, name='mypost'),
    path('delete/<str:id>/', delete, name="delete"),
    path('search/',search, name='search'),
<<<<<<< HEAD
    path('editpost/<str:id>/',editpost, name='editpost'),
=======
    path('home/likes/', views.likes, name='likes'),
>>>>>>> 10a7762507eab300f2f422ddf3cb4c14ad874dc2
]