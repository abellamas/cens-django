from django.urls import path
from . import views

urlpatterns = [
	path("", views.fines, name="fines"),
	path("inscripcion/", views.inscription, name="inscription")
]