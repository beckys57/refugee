from django.shortcuts import render

from .models import *
from skills.models import Category
from people.models import Level

def select_level(request, category_id):
	category = Category.objects.get(id=category_id)
	context = {
		'category': category,
		'levels': Level.objects.filter(category=category),
	}
	return render(request, 'listings/select_level.html', context)

def category_listings(request, category_id):
	category = Category.objects.get(id=category_id)
	level = request.GET.get('level')
	if level and not level == 'u': #Not all and not unknown level
		# listings = Listing.objects.filter(level=)
		level = Level.objects.get(id=level)
	listings = Listing.objects.all()
	context = {
		'listings': listings,
		'level': level,
	}
	return render(request, 'listings/listings.html', context)