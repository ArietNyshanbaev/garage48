from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User

class Cardstick(models.Model):
	""" Card info """

	card_id = models.CharField(max_length = 7)
	activated = models.BooleanField(default = False)
	telephone = models.CharField(max_length = 20,default = "")
	email = models.CharField(max_length = 50,default = "")
	name = models.CharField(max_length = 100,default = "")

	def __unicode__(self):
		return self.card_id

	class Meta:
		verbose_name = "каrta"
		verbose_name_plural = "каrty"

