from django import forms
from .models import musician
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class add_musician(forms.ModelForm):
    class Meta:
        model=musician
        fields='__all__'
class registations(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']