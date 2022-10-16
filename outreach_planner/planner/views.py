from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponseRedirect
=======
from django.contrib.auth.decorators import login_required
>>>>>>> test_views
from .models import Event
from .forms import VenueForm

@login_required(login_url='/users/login_user')
def home(request):
    event_list = Event.objects.all()
    return render(request, 'dashboard.html', 
<<<<<<< HEAD
    {'event_list': event_list})

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
=======
    {'event_list': event_list, 'username': request.user.username})
>>>>>>> test_views
