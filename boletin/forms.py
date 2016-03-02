from django import forms

class Registro(forms.Form):
	nombre = forms.CharField(max_length=100)
	edad = forms.IntegerField()