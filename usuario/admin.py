from django.contrib import admin

# Register your models here.
from models import usuarios, TodoArticulo

class AdminUsu(admin.ModelAdmin):
	list_display = ['__str__','apellidos','edad']
	class Meta:
		model = usuarios

class TodoAdmin(admin.ModelAdmin):
	list_display = ('nombre',)
	list_filter = ('nombre',)
	search_fields = ['nombre']
	inlines = [TodoArticulo]

admin.site.register(usuarios,AdminUsu)
admin.site.register(TodoArticulo)
