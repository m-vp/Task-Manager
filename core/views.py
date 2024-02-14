from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,login, logout
# Create your views here.

def signup(request):
    if request.method == 'POST':
        usr = request.POST['usrname']
        pwd = request.POST['password']
        user = User.objects.create_user(username=usr,password=pwd)
        user.save()
        return redirect('logins')
    return render(request,'signup.html')

def logins(request):
    if request.method == 'POST':
        usr = request.POST['usrname']
        pwd = request.POST['password']
        user = authenticate(request,username=usr,password=pwd)
        if user is not None:
            login(request,user)
            return redirect('todo')
        else:
            
            return redirect('login')
    return render(request,'login.html')

def todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        res = TODOLIST(title = title, user = request.user)
        res.save()
        ress = TODOLIST.objects.filter(user=request.user).order_by('-date')
        con = {'ress':ress}
        return render(request, 'todolist.html', con)
    ress = TODOLIST.objects.filter(user=request.user).order_by('-date')
    con = {'ress':ress, 'username': request.user.username}
    return render(request, 'todolist.html',con)

from django.shortcuts import render, get_object_or_404, redirect
from .models import TODOLIST

def edit(request, sr):
    # Get the TODOLIST object based on the provided 'sr'
    task = TODOLIST.objects.get(sr=sr)

    if request.method == 'POST':
        # Check if 'title' key exists in POST data
        if 'title' in request.POST:
            title = request.POST['title']
            
            # Update the TODOLIST object with the new title
            task.title = title
            task.save()

            # Redirect to the 'todo' view or wherever you want to go
            return redirect('todo')

    # If the request method is not POST, render the 'edit' template
    return render(request, 'edit.html', {'task': task})


def delete(request,sr):
    res = TODOLIST.objects.get(sr=sr)
    res.delete()
    return redirect(todo)

def signout(request):
    logout(request)
    return redirect('logins')