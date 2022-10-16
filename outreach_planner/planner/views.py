from django import forms
from django.forms import ModelForm
from django.shortcuts import render
<<<<<<< HEAD
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
=======
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
>>>>>>> 133e148aaad43b30af45617fb6f879225871eb13
from .models import Event
from .forms import VenueForm

@login_required(login_url='/users/login_user')
def home(request):
    event_list = Event.objects.all()
    return render(request, 'dashboard.html', 
    {'event_list': event_list})
<<<<<<< HEAD
>>>>>>> 26d6fbdf395c8a359d86a55d823e799c286f635c
=======

def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else: 
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'add_venue.html', {'form': form, 'submitted': submitted})
>>>>>>> 133e148aaad43b30af45617fb6f879225871eb13
