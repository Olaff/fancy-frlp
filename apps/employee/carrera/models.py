#-*-encoding:utf-8 -*-
#Models for Carrera
from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.utils.text import slugify
from django.utils.translation import gettext as _
from django.utils.encoding import smart_unicode
from django.core.urlresolvers import reverse

class Carrera(models.Model):
	options = (
             (1995, '1995'),
             (2008, '2008'),
         )
	nombre = models.CharField(max_length=50, verbose_name='Nombre de la carrera',help_text="Ingresar sólo la especialidad, sin tildes")
	tit_intermedio = models.CharField(max_length=50, verbose_name='Título intermedio', help_text='Puede dejarse en blanco', blank=True)
	planestudio = models.FileField(upload_to='alumnosweb/', blank='True', verbose_name="Plan de Estudio")
	year = models.IntegerField(max_length=4, default='', choices = options, verbose_name="Año")
	slug = AutoSlugField(_('slug'), max_length=50, unique=True, populate_from=('nombre',))
	
	def save(self, *args, **kwargs):
        	if not self.id:
                	#Only set the slug when the object is created.
            		self.slug = slugify(self.nombre) #Or whatever you want the slug to use
        	super(Carrera, self).save(*args, **kwargs)
		
	
	def get_title(self):
		#Returns career title depending its name
		if 'sistema' in self.nombre:
			return 'Ingenieria en %s de Informacion' % (self.nombre.title())
		else:
			return  'Ingenieria %s' % (self.nombre.title())
	
	def get_absolute_url(self):
		#Returns absolute url for details
		return reverse('carreras:carrera_details', args=[self.slug])
		
	
	def __unicode__(self):
		return smart_unicode(self.nombre)
