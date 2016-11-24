from __future__ import unicode_literals

from django.db import models
from skills.models import Category

class Profile(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)

	@property
	def full_name(self):
		return "{} {}".format(self.first_name, self.last_name)

class Helper(Profile):
	def __str__(self):
		return self.full_name

class Organisation(models.Model):
	name = models.CharField(max_length=255)
	telephone = models.CharField(max_length=50)
	def __str__(self):
		return self.name


class Level(models.Model):
	""" Existing skill level """
	name = models.CharField(max_length=255)
	category = models.ForeignKey(Category, null=True, blank=True)
	def __str__(self):
		return self.name