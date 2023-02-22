from django.contrib import admin
from . import models

@admin.register(models.Inscription)
class InscriptionAdmin(admin.ModelAdmin):
	list_display = ('created', 'dni', 'name', 'last_name')
# Register your models here.