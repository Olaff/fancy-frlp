from django.contrib import admin
from main_alumno.models import *
# Register your models here.

    
admin.site.register(Alumno)
admin.site.register(Catedra)
admin.site.register(Carrera)
admin.site.register(Comision)
admin.site.register(Horario)

