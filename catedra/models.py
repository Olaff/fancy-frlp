#-*-encoding:utf-8 -*-
#Models para Catedras 
from django.db import models
from django.utils.translation import gettext as _
from django_extensions.db.fields import AutoSlugField


class InfoCatedra(models.Model):
	nombre = models.CharField(max_length=50, verbose_name='Nombre')
	jefe_catedra = models.CharField(max_length=50, verbose_name='Jefe de Cátedra')
	jtp = models.CharField(max_length=50, verbose_name='Jefe de Trabajos Prácticos', blank=True)
	sitio = models.URLField(max_length=100, verbose_name="Sitio web", help_text="Sitio web de la página")
	slug = AutoSlugField(_('slug'), max_length=50, unique=True, populate_from=('nombre',))
	
	def __unicode__(self):
		return smart_unicode(self.nombre)
		
	def filename(self):
        	return os.path.basename(self.file.name)
				
	class Meta:
        	abstract = True
        	ordering = ['-nombre']
        	
class Catedra(InfoCatedra):
	nivel = models.CharField(max_length=2) 
	bool_choices = ((True, 'Sí'), (False, 'No'))	
	electiva = models.BooleanField(default ='', choices = bool_choices)	
	carrera = models.ForeignKey('carrera.Carrera', default='')
	sylabus = models.FileField(upload_to='alumnosweb/', blank=True)
	comisiones = models.ManyToManyField('comision.Comision', related_name="catedras", through = 'horario.Horario')
