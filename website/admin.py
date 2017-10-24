from django.contrib import admin
from .models import Action, OpenFireUser
from chat_app.models import UserToken

# Register your models here.

admin.site.register(Action)
admin.site.register(OpenFireUser)
admin.site.register(UserToken)
