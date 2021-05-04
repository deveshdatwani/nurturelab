from django.db import models
from datetime import datetime

# Create your models here.
class Advisor(models.Model):
	name = models.CharField(max_length=30, null=False)
	photo_url = models.CharField(max_length=200, null=False)

class Calls(models.Model):
	advisor = models.CharField(max_length=30, null=False)
	user = models.CharField(max_length=30, null=False)
	datetime = models.DateTimeField(null=False)