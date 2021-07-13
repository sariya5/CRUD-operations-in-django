from django.db import models
from django.urls import reverse

# Create your models here.

class student(models.Model):
	enrl_no = models.IntegerField(primary_key=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	age = models.CharField(max_length=100)
	batch = models.CharField(max_length=100)
	course = models.CharField(max_length=100)
	address = models.CharField(max_length=100)

	def __str__(self):
		return f'{self.enrl_no} student'

	def get_absolute_url(self):
		return reverse('home',kwargs={})	
	

		