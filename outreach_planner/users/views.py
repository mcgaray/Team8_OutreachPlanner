
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm
#from django.http import HttpResponseRedirect
#from .forms import RegisterUserForm





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