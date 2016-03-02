from django.shortcuts import render
from .forms import RegPrueba
# Create your views here.

def vistaPrueba(request):
	alfred = RegPrueba(request.POST or None)
	context = {
		'alfred':alfred
	}

	if alfred.is_valid():
		male = alfred.cleaned_data
		print male.get('ahorro')
		print male.get('aporte')

	return render(request,'prueba.html',context)