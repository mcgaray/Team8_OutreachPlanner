from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
<<<<<<< HEAD
    path('register_user', views.register_user, name="register")
=======
    path('add_venue', views.add_venue, name='add-venue'),
>>>>>>> 133e148aaad43b30af45617fb6f879225871eb13
]