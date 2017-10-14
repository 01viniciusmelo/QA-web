from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Action(models.Model):
    user = models.ForeignKey(User)
    action_text = models.TextField(blank=False, null=False)
    date_done = models.DateTimeField(auto_now=False, auto_now_add=True)


class OpenFireUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    owner = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField( auto_now=True)

    def __str__(self):

        if len(self.username) > 15:
            usn = self.username[:12] + "..."
        else:
            usn = self.username

        return "{} owned by {}".format(usn, self.owner.get_username())


    def __unicode__(self):

        if len(self.username) > 15:
            usn = self.username[:12] + "..."
        else:
            usn = self.username

        return "{} owned by {}".format(usn, self.owner.get_username())
