from django.shortcuts import render

from skills.models import Category
from .models import *

# Create your views here.
def language_select(request):
	print 'Lan'
	languages = Language.objects.all()
	context = {
		'languages': languages,
	}
	return render(request, 'core/language_select.html', context)

def category_select(request):
	print 'Cat'
	context = {
		'categories': Category.objects.all(),
	}
	return render(request, 'core/category_select.html', context)