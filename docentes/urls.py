from django.urls import path
from . import views

urlpatterns = [
	path("", views.docentes, name="docentes")
]