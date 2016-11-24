from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Language(models.Model):
	english_name = models.CharField(max_length=50, null=True, blank=True)
	native_name = models.CharField(max_length=50, null=True, blank=True)
	name_image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.english_name