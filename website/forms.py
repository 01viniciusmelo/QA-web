from django.contrib.auth.forms import AuthenticationForm
import django.forms as FormWidgets
from django import forms
from . import models


class OpenFireUserForm(ModelForm):
    class Meta:
        model = OpenFireUser
        fields = ('username', 'password', 'owner', 'created_on', 'updated_on', )
    