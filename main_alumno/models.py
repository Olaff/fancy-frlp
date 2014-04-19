#-*-encoding:utf-8 -*-
from django.db import models
from datetime import date
from django.contrib.admin import widgets    #Para Widgets en campos fecha
from django_extensions.db.fields import AutoSlugField
from django.utils.translation import gettext as _
from django.contrib.auth.signals import user_logged_in, user_logged_out  
from django.utils.encoding import smart_unicode

class InfoCatedra(models.Model):
	nombre = models.CharField(max_length=50, verbose_name='Nombre')
	jefe_catedra = models.CharField(max_length=50, verbose_name='Jefe de Cátedra')
	jtp = models.CharField(max_length=50, verbose_name='Jefe de Trabajos Prácticos', blank=True)
	slug = AutoSlugField(_('slug'), max_length=50, unique=True, populate_from=('nombre',))
	
	def __unicode__(self):
		return smart_unicode(self.nombre)
		
	def filename(self):
        	return os.path.basename(self.file.name)
				
	class Meta:
        	abstract = True
        	ordering = ['-nombre']
  	
#CLASES CONCRETAS 

class Carrera(models.Model):
	nombre = models.CharField(max_length=50, verbose_name='Nombre de la carrera',help_text="Ingresar sólo la especialidad, sin tildes")
	tit_intermedio = models.CharField(max_length=50, verbose_name='Título intermedio', help_text='Puede dejarse en blanco', blank=True)
	planestudio = models.FileField(upload_to='alumnosweb/', blank='True', verbose_name="Plan de Estudio")
	year = models.CharField(max_length=4, verbose_name="Año")
	slug = AutoSlugField(_('slug'), max_length=50, unique=True, populate_from=('nombre',))
	
	def __unicode__(self):
		return smart_unicode(self.nombre)
	
class Comision(models.Model):
	numero = models.CharField(max_length=100, default='',  verbose_name="Nº Comisión")
	turno = models.CharField(max_length=100, default='',  verbose_name="Turno") 
	nivel = models.CharField(max_length=2) #Uso interno, no se muestra al usuario 
	carrera = models.ForeignKey('Carrera') 
	
	
	def __unicode__(self):
		return smart_unicode(self.numero)
		
class Catedra(InfoCatedra):
	nivel = models.CharField(max_length=2) 
	bool_choices = ((True, 'Sí'), (False, 'No'))	
	electiva = models.BooleanField(default ='', choices = bool_choices)	
	carrera = models.ForeignKey('Carrera', default='')
	sylabus = models.FileField(upload_to='alumnosweb/', blank=True)
	comisiones = models.ManyToManyField('Comision', related_name="catedras", through = 'Horario')
	
	
class Horario(models.Model): 
	catedra = models.ForeignKey('Catedra')
	comision = models.ForeignKey('Comision', related_name='horarios')
	maniana, tarde, noche = 'maniana', 'tarde', 'noche'
	opt_turno = (
		(maniana, 'Mañana'),
		(tarde, 'Tarde'),
		(noche, 'Noche'),
	)
	lunes, martes, miercoles, jueves, viernes, sabado = 'lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado'
	opciones = (
		(lunes, 'Lunes'),
		(martes, 'Martes'),
		(miercoles, 'Miercoles'),
		(jueves, 'Jueves'),
		(viernes, 'Viernes'),
		(sabado, 'Sábado'),
	)
	prof_t = models.CharField(max_length=100, default='', verbose_name="Profesor de Teoría")
	prof_p = models.CharField(max_length=100, default='', verbose_name="Profesor de Práctica")
	ayudantes = models.CharField(max_length=50, verbose_name='Ayudantes', blank=True ,help_text='Separar con coma')
	dia_t = models.CharField(max_length=10,  null=True, default='', choices = opciones, verbose_name="Día teórica")	
	dia_p = models.CharField(max_length=10, blank=True, default='', choices = opciones, verbose_name="Día práctica")	
	hora_inicio_t = models.TimeField(null=True, verbose_name='Inicio teórica', help_text="HH:MM") 
	hora_fin_t = models.TimeField(null=True, verbose_name='Fin teórica',help_text="HH:MM")	
	hora_inicio_p = models.TimeField(null=True, blank=True, verbose_name='Inicio práctica', help_text="HH:MM")	
	hora_fin_p = models.TimeField(null=True, blank=True, verbose_name="Fin  práctica", help_text="HH:MM")
	
	def  __unicode__(self):
		return smart_unicode(self.comision) + smart_unicode (self.catedra)
		
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
	carrera = models.ForeignKey('Carrera', help_text="Seleccione la carrera")
	
	def __unicode__(self):
		return smart_unicode(self.apellido, self.nombres)
	
	        
        
class Cursada(models.Model):
	cursando, aprobado, libre = 'cursando','aprobado','libre'
	options = (
		(cursando, 'Cursando'),
		(aprobado, 'Aprobado'),
		(libre , 'Libre'),
	)
	estado = models.CharField(max_length=20, default='' ,verbose_name="Estado", choices = options)
	
