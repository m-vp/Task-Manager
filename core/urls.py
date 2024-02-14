from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.signup,name='signup'),
    path("login/",views.logins,name='logins'),
    path("todo/",views.todo,name='todo'), 
    path("edit/<int:sr>/",views.edit,name='edit'),
    path("del/<int:sr>/",views.delete,name='del'),
    path('signout/',views.signout,name = 'logout')
]