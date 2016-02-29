from django.contrib import admin

# Register your models here.
from models import estudiante, Registro_Materia

class AdminEstudiantes(admin.TabularInline):
	model = Registro_Materia
	extra = 0

class AdminMaterias(admin.ModelAdmin):
	list_display = ('nombre',)
	list_filter = ('apellidos',)
	search_fields = ['nombre']
	inlines = [AdminEstudiantes]

admin.site.register(estudiante,AdminMaterias)
admin.site.register(Registro_Materia)
