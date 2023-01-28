from django.shortcuts import render


# Create your views here.
def fines(request):
	return render(request, "fines.html", {"title": "Plan Fines"})
