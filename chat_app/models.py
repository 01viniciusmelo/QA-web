from django.db import models
from django.contrib.auth.models import User


# from django.core.validators import RegexValidator
# from django.utils.translation import ugettext as _


# TODO: make another model for handling uploaded files and a pivot table for a many to many field (?)
class UserToken(models.Model):
    # comma_sep_validator = RegexValidator(regex=r'^[-\w]+(?:,[-\w]*)*$', message=_('invalid set for module names'))
    token = models.CharField(max_length=32, unique=True, null=False, blank=False)
    max_queries = models.IntegerField(default=-1)
    user = models.ForeignKey(User)
    bot_module_name = models.CharField(max_length=32, default='base_bot')
    bot_class_name = models.CharField(max_length=32, default='SampleBot')
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now=True)
