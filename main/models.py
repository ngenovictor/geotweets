from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hashtags(models.Model):
	value = models.CharField(max_length=30)
	user = models.ForeignKey(User,on_delete=models.CASCADE, default=User.username)
	date = models.DateTimeField(auto_now=False, auto_now_add=False)
