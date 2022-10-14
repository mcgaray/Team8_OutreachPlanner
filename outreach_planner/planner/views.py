from django.shortcuts import render
from .models import Event


def home(request):
    event_list = Event.objects.all()
    return render(request, 'dashboard.html', 
    {'event_list': event_list})