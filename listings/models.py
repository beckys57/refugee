from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from skills.models import Category, Skill
from people.models import *
# from skills.models import Category, Skill

class Listing(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	organisation = models.ForeignKey(Organisation, null=True, blank=True)
	skills = models.ManyToManyField(Skill)
	categories = models.ManyToManyField(Category)
	accredited = models.BooleanField(default=False)
	date = models.DateField(null=True, blank=True)
	levels = models.ManyToManyField(Level)

class Offer(Listing):
	availability = models.CharField(max_length=21, null=True, blank=True) # Series of 1s and 0s for availability from Mon-Sun 3 slots a day?

class Request(Listing):
	deadline = models.DateField(null=True, blank=True)


class Slots(models.Model):
	DAYS = [
		(0, 'Monday'),
		(1, 'Tuesday'),
		(2, 'Wednesday'),
		(3, 'Thursday'),
		(4, 'Friday'),
		(5, 'Saturday'),
		(6, 'Sunday'),
	]
	day = models.IntegerField(choices=DAYS)
	start = models.CharField(max_length=10, null=True, blank=True)
	end = models.CharField(max_length=10, null=True, blank=True)
	listing = models.ForeignKey('Listing', null=True, blank=True)