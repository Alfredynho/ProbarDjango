from django.shortcuts import render
from .forms import Registro
# Create your views here.
#Aqui declaramos las vistas
#se utiliza el request para solicitar algo
#con el response se regresa o responde
def inicio(request):
	form = Registro(request.POST or None)
	context = {
		'form':form
	}

	if form.is_valid():
		male = form.cleaned_data
		print male.get('nombre')
		print male.get('edad')
		print male.get('otro')

	return render(request,"index.html",context)