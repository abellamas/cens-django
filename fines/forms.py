from django import forms
from django.forms import ModelForm
from .models import Inscription


class InscriptionForm(ModelForm):

	class Meta:
		model = Inscription
		fields = "__all__"
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'autocapitalize': 'characters'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control', 'autocapitalize': 'characters'}),
			'dni': forms.TextInput(attrs={'class': 'form-control'}),
			'nationality': forms.Select(attrs={'class': 'form-select'}),
			'gender': forms.Select(attrs={'class': 'form-select'}),
			'birthday': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
			'address': forms.TextInput(attrs={'class': 'form-control'}),
			'neighborhood': forms.Select(attrs={'class': 'form-select'}),
			'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@gmail.com'}),
			'cellphone_1': forms.TextInput(attrs={'class': 'form-control'}),
			'cellphone_2': forms.TextInput(attrs={'class': 'form-control'}),
		}
