from .models import member
from django import forms

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model= member
        fields= ('first_name',
    'last_name',
    'username',
    'password',
    'post',
    'mail',
    'phone'
    )
