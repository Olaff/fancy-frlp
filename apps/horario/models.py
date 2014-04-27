#-*-encoding:utf-8 -*-
#Models for Horario
from django.db import models
from datetime import date
from django.utils.encoding import smart_unicode
from apps.comision.models import Comision

class Horario(models.Model): 
	catedra = models.ForeignKey('catedra.Catedra')
	comision = models.ForeignKey('comision.Comision', related_name='horarios')
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
