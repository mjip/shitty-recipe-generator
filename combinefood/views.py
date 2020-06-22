from django.shortcuts import render
from django.http import HttpResponse

from .models import Food, Recipe, Sauce, Spice

def index(request):
	protein = Food.objects.filter(category='protein').order_by('?').first()
	vegs = Food.objects.filter(category='vegetable').order_by('?')
	veg1 = vegs.first()
	veg2 = vegs.last()
	carb = Food.objects.filter(category='carb').order_by('?').first()

	context = {
		'protein_name': protein.name,
		'carb_name': carb.name,
		'veg1_name': veg1.name,
		'veg2_name': veg2.name,
	}

	return render(request, 'combinefood/index.html', context)
