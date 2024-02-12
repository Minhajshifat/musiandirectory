from django import forms
from .models import album
class add_album(forms.ModelForm):
    class Meta:
        model=album
        fields='__all__'
        