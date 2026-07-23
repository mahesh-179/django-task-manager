from django import forms 
from .models import Profile

class ProfileCreate(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']