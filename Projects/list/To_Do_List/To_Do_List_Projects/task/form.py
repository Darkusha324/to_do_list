from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Task

class FormTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']



class RegisterUserForm(UserCreationForm):
    password2 = forms.CharField(widget=forms.PasswordInput,help_text='')
    class Meta:
        model = User
        fields = ['username','password1','password2']
        help_texts = {
            'username':'',
            'password1':'',
            'password2': ''
        }

