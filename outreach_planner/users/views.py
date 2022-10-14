
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm 
from .forms import RegisterUserForm
from django import forms





def login_user(request):
    if request.method == "POST":
        input_email = request.POST['input_email']
        input_password = request.POST['input_password']
        user = authenticate(request, input_email=input_email, input_password=input_password)
        if user is not None:
                login(request, user)
                return redirect('home')
        else:
                messages.success(request,("There was an error. Please try again."))
                return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1', 'password2']
            user = authenticate(email = email, password=password )
            login(request, user)
            messages.success(request, ("Registered"))
            return redirect('login')
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register_user.html', {'form':form})

