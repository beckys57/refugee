from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Skill(models.Model):
	category = models.ForeignKey('Category')
	name = models.CharField(max_length=50)