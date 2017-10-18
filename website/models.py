from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import ugettext as _


# Create your models here.

class Action(models.Model):
    user = models.ForeignKey(User)
    action_text = models.TextField(blank=False, null=False)
    date_done = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        msg = '{} done via {}.'.format(self.action_text, self.user.name)
        return msg


class OpenFireUser(models.Model):
    # Translators: phone validation error
    phone_number_validator = RegexValidator(regex=r'^09(1|3|0)(\d){8}$',
                                            message=_('username must be a valid phone number.'))
    username = models.CharField(max_length=50, unique=True, validators=[phone_number_validator])
    password = models.CharField(max_length=50)
    owner = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):

        if len(self.username) > 15:
            usn = self.username[:12] + "..."
        else:
            usn = self.username

        return "{} owned by {}".format(usn, self.owner.get_username())
