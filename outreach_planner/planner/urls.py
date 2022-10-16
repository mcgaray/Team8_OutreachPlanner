from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_venue', views.add_venue, name='add-venue'),
    path('list_venue', views.list_venue, name='list-venue'),
    path('show_venue/<venue_id>', views.show_venue, name='show-venue'),
    path('search_venue', views.search_venue, name='search-venue'),
    path('update_venue/<venue_id>', views.update_venue, name='update-venue'),
]