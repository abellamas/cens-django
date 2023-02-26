from django.db import models
from fines.models import Person
# Create your models here.

class Professor(Person):
	cuil = models.CharField(max_length=10, blank=False, unique=True, verbose_name="CUIL")

	class Meta:
		verbose_name = 'Profesor'
		verbose_name_plural = 'Profesores'