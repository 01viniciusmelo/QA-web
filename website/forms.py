from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from django import forms
from .models import OpenFireUser


class OpenFireUserForm(ModelForm):
    class Meta:
        model = OpenFireUser
        fields = ('username', 'password', 'owner',)
    