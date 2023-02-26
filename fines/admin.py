from django.contrib import admin
from . import models


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
	search_fields = ('dni',)
	list_display = ('dni', 'name', 'last_name', 'created')

@admin.register(models.Commission)
class CommissionAdmin(admin.ModelAdmin):
	list_display = ('commission', 'id_commission', 'orientation', 'campus', 'status')

@admin.register(models.Orientation)
class OrientationAdmin(admin.ModelAdmin):
	list_display = ('orientation', 'resolution')
@admin.register(models.Campus)
class CampusAdmin(admin.ModelAdmin):
	list_display = ('campus', 'address', 'referent', 'phone_number')
@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
	list_display = ('subject', 'hours', 'orientation', 'period')

@admin.register(models.Legajo)
class LegajoAdmin(admin.ModelAdmin):
	list_display = ('student', 'book', 'folio')
# Register your models here.