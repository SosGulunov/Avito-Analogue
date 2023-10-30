import random

from django.shortcuts import render, redirect
from .models import Ad, Person
from .form import PostForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate

def home(request):
    r = random.randint(1, 15)
    numbers = [1,1,1,1,1]
    count = len(numbers)
    ad = Ad.objects.all()
    person = Person.objects.all()
    return render(request, 'front/index.html', {'ad': ad, 'person': person, 'random': r, 'randoma': numbers, 'count': count})


def add(request):
    form = PostForm()
    return render(request, "front/add.html",  {'form': form})

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'front/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password2'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'front/signupuser.html', {'form': UserCreationForm(), 'error': 'That username has already been taken. Please choose a new username'})

        else:
            return render(request, 'front/signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'front/loginuser.html',{'form': AuthenticationForm()})
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request, 'front/loginuser.html', {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('currenttodos')