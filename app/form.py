from django import forms  
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'photo', 'gender', 'pnum', 'job_role']
    