from django import forms
from django.forms import ModelForm
from django.shortcuts import render
<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .models import Volunteer
from .forms import RegisterUserForm

def home(request):
    return render(request, 'home.html', {})

def register_user(request):
    submitted = False
    form = RegisterUserForm
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_user?sumbitted=True')
    else:
        form = RegisterUserForm
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'auth/register_user.html', {'form':form, 'submitted':submitted})
=======
from .models import Event


def home(request):
    event_list = Event.objects.all()
    return render(request, 'dashboard.html', 
    {'event_list': event_list})
>>>>>>> 26d6fbdf395c8a359d86a55d823e799c286f635c
