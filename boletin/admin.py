from django.contrib import admin
from .models import Registro_docente
# Register your models here.
class AdminRegistrado(admin.ModelAdmin):
	list_display = ['__str__','nombre','email']
	class Meta:
		model = Registro_docente

admin.site.register(Registro_docente,AdminRegistrado)