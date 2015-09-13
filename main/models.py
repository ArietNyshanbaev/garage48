from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User

class Cardstick(models.Model):
	""" Card info """

	card_id = models.CharField(max_length = 7, unique=True)
	activated = models.BooleanField(default = False)
	telephone = models.CharField(max_length = 20,default = "",null=True, blank=True)
	email = models.CharField(max_length = 50,default = "",null=True, blank=True)
	name = models.CharField(max_length = 100,default = "",null=True, blank=True)

	def __unicode__(self):
		return self.card_id

	class Meta:
		verbose_name = "Карта"
		verbose_name_plural = "Карты"