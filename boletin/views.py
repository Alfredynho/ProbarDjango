from django.shortcuts import render

# Create your views here.
#Aqui declaramos las vistas
#se utiliza el request para solicitar algo
#con el response se regresa o responde
def inicio(request):
	return render(request,"index.html",{})