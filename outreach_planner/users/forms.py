from django.contrib.auth.forms import ModelForms
from django.contrib.auth.models import User
from django import forms
from planner.models import Volunteer



class RegisterUserForm(ModelForms):
    class Meta: 
        model = Volunteer
        fields = ('username','first_name','last_name','email')