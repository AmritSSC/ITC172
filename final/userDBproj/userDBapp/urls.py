from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getTypes/', views.getTypes, name='types'),
    path('getUsers/', views.getUsers, name='members'),
    path('userDetails/<int:id>', views.userDetails, name='userdetails'),
]