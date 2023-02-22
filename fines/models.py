from django.db import models
from datetime import datetime


# Create your models here.
class Inscription(models.Model):
	COUNTRY_CHOICES = [
		('ARG','Argentina'),
		('BOL','Boliviana'),
		('BRA','Brasilera'),
		('CHI','Chilena'),
		('COL','Colombiana'),
		('ECU','Ecuatoriana'),
		('PAR','Paraguaya'),
		('PER','Peruana'),
		('URU','Uruguaya'),
		('VEN','Venezolana'),
		('OTRO','Otro')
	]
	GENDER_CHOICES = [
		('Femenino','Femenino'),
		('Masculino', 'Masculino'),
		('No Binario', 'No Binario')
	]

	NEIGHBORHOOD_CHOICES = [
		('Avellaneda', 'Avellaneda'),
		('Barrio Pampa', 'Barrio Pampa'),
		('Caraza', 'Caraza'),
		('C.A.B.A.', 'C.A.B.A.'),
		('El pueblito/Radio Estación', 'El pueblito/Radio Estación'),
		('Gerli', 'Gerli'),
		('Lanús Este', 'Lanús Este'),
		('Lanús Oeste', 'Lanús Oeste'),
		('L. de Zamora', 'L. de Zamora'),
		('Valentin Alsina', 'Valentin Alsina'),
		('Villa Diamante', 'Villa Diamante'),
		('Villa Jardín', 'Villa Jardín')
	]
	created = models.DateTimeField(auto_now_add=True, verbose_name="Inscripción")
	name = models.CharField(max_length=40, blank=False, verbose_name="Nombre/s")
	last_name = models.CharField(max_length=40, blank=False, verbose_name="Apellido/s")
	dni = models.IntegerField(blank=False, verbose_name="DNI", unique=True)
	nationality = models.CharField(max_length=12, choices=COUNTRY_CHOICES, blank=True, null=False,
									verbose_name="Nacionalidad")
	gender = models.CharField(max_length=10,choices=GENDER_CHOICES, blank=True, null=False, verbose_name="Genero")
	birthday = models.DateField(verbose_name="Fecha de nacimiento", blank=False)
	address = models.CharField(max_length=50, blank=True, verbose_name="Domicilio")
	neighborhood = models.CharField(max_length=30, blank=False, choices=NEIGHBORHOOD_CHOICES, verbose_name="Localidad/Barrio")
	email = models.EmailField(max_length=254, blank=False, verbose_name="Correo electrónico")
	cellphone_1 = models.CharField(max_length=10, blank=False)
	cellphone_2 = models.CharField(max_length=10, blank=True,null=False)

	class Meta:
		verbose_name = "Inscripción"
		verbose_name_plural = "Inscripciónes"
