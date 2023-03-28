from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

class Orientation(models.Model):
	orientation = models.CharField(max_length=40, verbose_name="Orientación")
	resolution = models.CharField(max_length=10, verbose_name="N° Resolución")

	class Meta:
		verbose_name = "Orientación"
		verbose_name_plural = "Orientaciones"

	def __str__(self):
		return self.orientation

class Subject(models.Model):
	PERIOD_CHOICE = [('1°1C', '1°1C'), ('1°2C', '1°2C'), ('2°1C', '2°1C'), ('2°2C', '2°2C'),
					('3°1C', '3°1C'), ('3°2C', '3°2C')]

	subject = models.CharField(max_length=40, verbose_name="Asignatura")
	hours = models.IntegerField(verbose_name="Horas Cátedra")
	orientation = models.ForeignKey(Orientation, on_delete=models.CASCADE, verbose_name='Orientación')
	period = models.CharField(max_length=4, choices=PERIOD_CHOICE, verbose_name='Cuatrimestre')

	class Meta:
		verbose_name = "Materias"
		verbose_name_plural = "Materias"

	def __str__(self):
		return self.subject

class Campus(models.Model):
	campus = models.CharField(max_length=30, verbose_name='Sede')
	address = models.CharField(max_length=35, verbose_name='Dirección')
	referent = models.CharField(max_length=15, verbose_name='Referente')
	phone_number = models.CharField(max_length=10)

	class Meta:
		verbose_name = "Sede"
		verbose_name_plural = "Sedes"

	def __str__(self):
		return self.campus

class Commission(models.Model):
	STATUS_CHOICES = [('Activa', 'Activa'),
					  ('Reagrupada', 'Reagrupada'),
					  ('Cerrada', 'Cerrada'),
					  ('Egresada', 'Egresada')]

	id_commission = models.CharField(max_length=11, primary_key=True, verbose_name='ID Comisión')
	commission = models.CharField(max_length=15, verbose_name='Comisión')
	orientation = models.ForeignKey(Orientation, on_delete=models.SET('Orientación Eliminada'))
	campus = models.ForeignKey(Campus, on_delete=models.SET('Sede Eliminada'))
	status = models.CharField(max_length=10, choices=STATUS_CHOICES)

	class Meta:
		verbose_name = "Comisión"
		verbose_name_plural = "Comisiones"

	def __str__(self):
		return self.commission

# Create your models here.
class Person(models.Model):
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
		('F','Femenino'),
		('M', 'Masculino'),
		('X', 'No Binario')
	]
	dni = models.IntegerField(primary_key=True, validators=[MinValueValidator(0), MaxValueValidator(99999999)],
								verbose_name="DNI")
	name = models.CharField(max_length=50, blank=False, verbose_name="Nombre/s")
	last_name = models.CharField(max_length=50, blank=False, verbose_name="Apellido/s")
	birthday = models.DateField(verbose_name="Fecha de nacimiento", blank=False)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=False, verbose_name="Género")
	nationality = models.CharField(max_length=12, choices=COUNTRY_CHOICES, blank=True, null=False,
								   verbose_name="Nacionalidad")
	email = models.EmailField(max_length=254, blank=False, verbose_name="Correo electrónico")
	cellphone = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999999999)], verbose_name="Celular")

	class Meta:
		abstract = True

class Student(Person):

	PROVINCE_CHOICES = [
		('Buenos Aires', 'Buenos Aires'),
		('C.A.B.A.', 'C.A.B.A.'),
		('Otro país', 'Otro país'),
		('Catamarca','Catamarca'),
		('Chaco', 'Chaco'),
		('Chubut', 'Chubut'),
		('Cordoba', 'Cordoba'),
		('Corrientes', 'Corrientes'),
		('Entre Ríos', 'Entre Ríos'),
		('Formosa', 'Formosa'),
		('Jujuy', 'Jujuy'),
		('La Pampa', 'La Pampa'),
		('La Rioja', 'La Rioja'),
		('Mendoza', 'Mendoza'),
		('Misiones', 'Misiones'),
		('Río Negro', 'Río Negro'),
		('Salta', 'Salta'),
		('San Juan', 'San Juan'),
		('San Luis', 'San Luis'),
		('Santa Cruz', 'Santa Cruz'),
		('Santa Fé', 'Santa Fé'),
		('Santiago del Estero', 'Santiago del Estero'),
		('Tierra del Fuego e Islas del Sur', 'Tierra del Fuego e Islas del Sur'),
		('Tucuman','Tucuman'),
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

	OLD_STUDIES_CHOICES = [
		('Primaria completa', 'Primaria 6to o 7mo grado completo'),
		('1ro de 6 años', '1ro secundaria común de 6 años o técnica de 7 años'),
		('2do de 6 años', '2do secundaria común de 6 años o técnica de 7 años'),
		('3ro de 6 años', '3ro secundaria común de 6 años o técnica de 7 años'),
		('4to de 6 años', '4to secundaria común de 6 años o técnica de 7 años'),
		('5to de 6 años', '5to secundaria común de 6 años o técnica de 7 años'),
		('1ro de 5 años', '1ro secundaria común de 5 años o técnica de 6 años'),
		('2do de 5 años', '1ro secundaria común de 5 años o técnica de 6 años'),
		('3ro de 5 años', '1ro secundaria común de 5 años o técnica de 6 años'),
		('4to de 5 años', '1ro secundaria común de 5 años o técnica de 6 años'),
		('7mo EGB', '7mo año EGB'),
		('8vo EGB', '8vo año EGB'),
		('9no EGB', '9no año EGB'),
		('9no EGBA', '9no/3er ciclo EGB Adultos'),
		('1ro Polimodal', '1ro polimodal'),
		('2do Polimodal', '2do polimodal'),
		('1ro ESB', '1ro secundaria básica ESB'),
		('2do ESB', '2ro secundaria básica ESB'),
		('3ro ESB', '3ro secundaria básica ESB'),
		('1ro BAOT/BAO', '1ro BAOT/BAO'),
		('2do BAOT/BAO', '1ro BAOT/BAO'),
	]

	SHIFT_CHOICES = [
		('TM', 'Turno Mañana 8 hs a 12 hs aprox.'),
		('TT', 'Turno Tarde 13 hs a 17 hs aprox.'),
		('TV', 'Turno Vespertino/Noche 18 hs a 22 hs aprox.')
	]

	# FOREING KEY
	commission = models.ManyToManyField(Commission)
	# another fields
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Inscripción")
	place_birdth = models.CharField(max_length=100, verbose_name="Lugar de Nacimiento", blank=False)
	address = models.CharField(max_length=100, blank=True, verbose_name="Domicilio")
	neighborhood = models.CharField(max_length=30, blank=False, choices=NEIGHBORHOOD_CHOICES, verbose_name="Localidad/Barrio")
	cellphone_2 = models.CharField(max_length=10, blank=True, null=False, verbose_name="Celular 2")
	level_studies = models.CharField(max_length=20, choices=OLD_STUDIES_CHOICES, verbose_name="Estudios Previos")
	subjets_owed = models.TextField(verbose_name="Materias Adeudadas", blank=True)
	college = models.CharField(max_length=50, verbose_name="Colegio")
	college_country = models.CharField(max_length=12, choices=Person.COUNTRY_CHOICES, verbose_name="País del colegio")
	college_province = models.CharField(max_length=35, choices=PROVINCE_CHOICES, verbose_name='Provincia del colegio')
	college_city = models.CharField(max_length=30, verbose_name="Ciudad del colegio")
	prefered_shift = models.CharField(max_length=45, choices=SHIFT_CHOICES, verbose_name='Turno de preferencia')
	prefered_campus = models.CharField(max_length=30, verbose_name='Sede de preferencia')


	class Meta:
		verbose_name = "Alumno"
		verbose_name_plural = "Alumnos"

	def __str__(self):
		return f'{self.dni} - {self.last_name} {self.name}'


class Legajo(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Estudiante")
	orientation = models.ForeignKey(Orientation, on_delete=models.CASCADE, verbose_name="Orientación")
	book = models.IntegerField(verbose_name="Libro")
	folio = models.IntegerField(verbose_name="Folio")
	dni_copy = models.BooleanField(verbose_name="DNI Copia")
	p_nac_copy = models.BooleanField(verbose_name="P. Nac. Copia")
	certified = models.BooleanField(verbose_name="Certificado de estudios")
	constancia = models.BooleanField(verbose_name="Constancia")
	obs = models.TextField(verbose_name="Observaciones")
	class Meta:
		verbose_name = "Legajo"
		verbose_name_plural = "Legajos"

