from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import ugettext as _


# Create your models here.
class UserToken(models.Model):
    comma_sep_validator = RegexValidator(regex=r'^[-\w]+(?:,[-\w]*)*$', message=_('invalid set for module names'))
    token = models.CharField(max_length=32, unique=True)
    max_queries = models.IntegerField(default=-1)
    user = models.ForeignKey(User)
    bot_modules = models.TextField(validators=[comma_sep_validator])
