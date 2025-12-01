from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.messages.context_processors import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pymsgbox import password
from requests import post

from .models import Task
from .form import FormTask, RegisterUserForm


def task(request):
    taski = Task.objects.filter(user=request.user)
    return render(request,'task/task.html',{'taski':taski})



def form_task(request):
    if request.method == 'POST':
        form = FormTask(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            form.save()
            return redirect('task')
    else:
        form = FormTask()
    return render(request,'task/formtask.html',{'form':form})


def delete_task(request,id):
    task = Task.objects.filter(pk=id)
    task.delete()
    return redirect('task')

def complet_task(request,id):
    task = Task.objects.get(pk=id)
    if request.method=='POST':
        if task.is_published == False:
            task.is_published = True
            task.save()
            return redirect('task')


def uncomplet_task(request,id):
    task = Task.objects.get(pk=id)
    if request.method=='POST':
        if task.is_published == True:
            task.is_published = False
            task.save()
            return redirect('task')


def test(request):
    model = Task.objects.all()
    return render(request,'task/test.html',{'model':model})

def register(request, ):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterUserForm()
    return render(request, 'register/register.html', {'form': form})

def login_user(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('task')
    else:
        return render(request,'login/login.html',{'error':"Невірні данні"})

    return render(request,'login/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

