from django import forms

class RegPrueba(forms.Form):
	ahorro = forms.DecimalField()
	aporte = forms.IntegerField()