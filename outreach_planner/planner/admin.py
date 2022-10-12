from django.contrib import admin

# Registered models.

from .models import Venue
from .models import Volunteer
from .models import Event

admin.site.register(Venue)
admin.site.register(Volunteer)
admin.site.register(Event)