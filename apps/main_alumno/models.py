#-*-encoding:utf-8 -*-
#Models for Alumno 
from django.db import models
from datetime import date
from django.contrib.admin import widgets    #Para Widgets en campos fecha
from django_extensions.db.fields import AutoSlugField
from django.utils.translation import gettext as _
from django.utils.encoding import smart_unicode
from apps.carrera.models import Carrera  	
		
class  Alumno(models.Model):
	apellido = models.CharField(max_length=30, verbose_name="Apellido")
	nombres = models.CharField(max_length=50, verbose_name="Nombres")
	fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
	dni= models.CharField(max_length=8, null=False, verbose_name="DNI")
	lugar = models.CharField(max_length=50, help_text="Lugar de nacimiento")
	domicilio = models.CharField(max_length=50)
	localidad = models.CharField(max_length=25)
	telefono = models.CharField(max_length=20, verbose_name="Teléfono", help_text="Código de área - teléfono")
	celular = models.CharField(max_length=20)	
	legajo = models.CharField(max_length=50, unique=True)	
	mail = models.EmailField()
	slug = AutoSlugField(_('slug'), max_length=50, unique=True, populate_from=('apellido',))
	carrera = models.ForeignKey('carrera.Carrera', help_text="Seleccione la carrera")
	
	def __unicode__(self):
		return smart_unicode(self.apellido, self.nombres)
	

	
