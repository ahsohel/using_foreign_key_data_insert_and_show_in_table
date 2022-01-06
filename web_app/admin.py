from django.contrib import admin
from  . models import student
from . models import result
# Register your models here.

class dis_form_models(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll']

admin.site.register(student, dis_form_models)



class dis_form_models(admin.ModelAdmin):
    list_display = ['id', 'student_info', 'Status']

admin.site.register(result, dis_form_models)