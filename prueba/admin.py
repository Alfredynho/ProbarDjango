from django.contrib import admin
from .models import Prueba
# Register your models here.
#esto es un cambio
#comentario prueba
class mostrar(admin.ModelAdmin):
	list_display = ['__str__','edad']
	class Meta:
		model = Prueba

admin.site.register(Prueba,mostrar)