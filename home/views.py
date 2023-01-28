from django.shortcuts import render


# Create your views here.
def index(request):
	return render(request, "index.html", {"title": "CENTRO EDUCATIVO DE NIVEL SECUNDARIO N° 451"})
