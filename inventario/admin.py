from django.contrib import admin
from .models import estudiante
# Register your models here.

class RegStudent(admin.ModelAdmin):
	list_display = [
		'estado_dia'
	]
	class Meta:
		model = estudiante

admin.site.register(estudiante,RegStudent)