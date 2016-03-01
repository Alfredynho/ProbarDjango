from django.contrib import admin
from .models import Student
# Register your models here.

class RegStudent(admin.ModelAdmin):
	list_display = [
		'year_in_school'
	]
	class Meta:
		model = Student

admin.site.register(Student,RegStudent)