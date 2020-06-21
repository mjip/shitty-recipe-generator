from django.db import models

FOOD_CATS = (
	('protein', 'Protein'),
	('carb', 'Carb'),
	('vegetable', 'Vegetable'),
	('fruit', 'Fruit'),
)

class Food(models.Model):
	name = models.CharField(max_length=50)
	category = models.CharField(max_length=9, choices=FOOD_CATS)

	def __str__(self):
		return self.name + ", " + self.category

class Sauce(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Spice(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Recipe(models.Model):
	text = models.CharField(max_length=500)

	def __str__(self):
		return self.text
