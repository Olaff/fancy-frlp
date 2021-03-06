#-*-encoding:utf-8 -*-
#Models para Catedras 
from django.db import models
from django.utils.translation import gettext as _
from django_extensions.db.fields import AutoSlugField
from django.utils.text import slugify
from django.utils.encoding import smart_unicode
from django.core.urlresolvers import reverse


class InfoCatedra(models.Model):
	class Meta:
        	abstract = True
        	ordering = ['-nombre']
        	
	nombre = models.CharField(max_length=50, verbose_name='Nombre')
	jefe_catedra = models.CharField(max_length=50, verbose_name='Jefe de Cátedra')
	jtp = models.CharField(max_length=50, verbose_name='Jefe de Trabajos Prácticos', blank=True)
	sitio = models.URLField(max_length=100, verbose_name="Sitio web", help_text="Sitio web de la cátedra")
	slug = AutoSlugField(_('slug'), max_length=50, unique=True, populate_from=('nombre',))
	
	def __unicode__(self):
		return smart_unicode(self.nombre)
		
	def filename(self):
        	return os.path.basename(self.file.name)
        	
        def save(self, *args, **kwargs):
        	if not self.id:
                	#Only set the slug when the object is created.
            		self.slug = slugify(self.nombre) #Or whatever you want the slug to use
        	super(Catedra, self).save(*args, **kwargs)
        	
class Catedra(InfoCatedra):
	options_nivel = (
             ('1', '1'),
             ('2', '2'),
             ('3', '3'),
             ('4', '4'),
             ('5', '5'),
         )
	nivel = models.CharField(max_length=2,choices = options_nivel)
	correlativas = models.ManyToManyField('self', symmetrical=False, blank=True, related_name="correlate", verbose_name="Correlativas") 
	bool_choices = ((True, 'Sí'), (False, 'No'))	
	electiva = models.BooleanField(default ='', choices = bool_choices)	
	carrera = models.ForeignKey('carrera.Carrera', default='')
	sylabus = models.FileField(upload_to='alumnosweb/', blank=True)
	comisiones = models.ManyToManyField('comision.Comision', related_name="catedras", through = 'horario.Horario')
	
	def get_absolute_url(self):
		return reverse('catedras:catedra_details', args=[self.slug])
