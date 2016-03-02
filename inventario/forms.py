from django import forms

class RegInventario(forms.Form):
	nombre = forms.CharField(max_length=200)
	apellido = forms.CharField(max_length=20)
	edad = forms.IntegerField()

