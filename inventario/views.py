from django.shortcuts import render
from .forms import RegInventario
# Create your views here.

def prueba(request):
	form = RegInventario(request.POST or None)
	context = {
		'form':form
	}


	if form.is_valid():
		male = form.cleaned_data
		print male.get('nombre')
		print male.get('apellido')
		print male.get('edad')

	return render(request,'inventario.html',context)