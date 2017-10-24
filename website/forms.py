from django.forms import ModelForm
from .models import OpenFireUser
from chat_app.models import UserToken


class OpenFireUserForm(ModelForm):
    class Meta:
        model = OpenFireUser
        fields = ('username', 'password', 'owner',)


class UserTokenForm(ModelForm):
    class Meta:
        model = UserToken
        fields = ('bot_module_name', 'bot_class_name', 'user',)
