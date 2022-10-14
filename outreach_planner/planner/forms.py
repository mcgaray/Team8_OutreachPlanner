from django import forms
from django.forms import ModelForm
from .models import Volunteer


#create a user
class RegisterUserForm(ModelForm):
    class Meta: 
        model = Volunteer
        fields = ('first_name','last_name','email')