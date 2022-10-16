
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm
#from django.http import HttpResponseRedirect
#from .forms import RegisterUserForm





def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
                login(request, user)
                return redirect('home')
        else:
                messages.success(request,("Invalid input. Please try again."))
                return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request,("Logged out. See you next time!"))
    return redirect('login')

#def register_user(request):
#    submitted = False
 #   if request.method == "POST":
 #       form = RegisterUserForm(request.POST)
 #       if form.is_valid():
  #          form.save()
 #           return HttpResponseRedirect('/register_user?sumbitted=True')
 #   else:
 #       form = RegisterUserForm
  #      if 'submitted' in request.GET:
  #          submitted = True
  #  return render(request, 'authenticate/register_user.html', {'form':form, 'submitted':submitted})