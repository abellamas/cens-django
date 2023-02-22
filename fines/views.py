from django.shortcuts import render
from .forms import InscriptionForm
from django.http import HttpResponseRedirect

# Create your views here.
def fines(request):
	return render(request, "fines.html", {"title": "Plan Fines"})

def inscription(request):
	submitted = False
	if request.method == "POST":
		form = InscriptionForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/fines/inscripcion?submitted=True')
	else:
		form = InscriptionForm()
		if 'submitted' in request.GET:
			submitted = True

	return render(request, "form_inscription.html", {'form': form, 'submitted': submitted})