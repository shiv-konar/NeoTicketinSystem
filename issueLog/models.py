from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

import datetime

# Create your models here.


class Client(models.Model):
    client_name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.client_name


class Log(models.Model):
    client_name = models.ForeignKey(Client)
    issue_description = models.TextField(max_length=200)
    issued_by = models.ForeignKey(User)
    issued_on = models.DateField(default=datetime.datetime.now)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.issue_description


