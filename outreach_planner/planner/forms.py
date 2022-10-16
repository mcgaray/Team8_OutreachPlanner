from django import forms
<<<<<<< HEAD
from django.forms import ModelForm
from .models import Volunteer


#create a user
class RegisterUserForm(ModelForm):
    class Meta: 
        model = Volunteer
        fields = ('first_name','last_name','email')
=======
from django import forms
from django.forms import EmailField, EmailInput, ModelForm
from .models import Venue

#Venue Form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = "__all__"
        labels = {
            'venue_name': '',
            'address': '',
            'web_link': '',
            'phone': '',
            'email': '',
        }
        widgets = {
            'venue_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'web_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Web Link'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Contact Email'}),

        }
>>>>>>> 133e148aaad43b30af45617fb6f879225871eb13
