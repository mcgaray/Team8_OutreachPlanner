from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Event

@login_required(login_url='/users/login_user')
def home(request):
    event_list = Event.objects.all()
    return render(request, 'dashboard.html', 
    {'event_list': event_list, 'username': request.user.username})