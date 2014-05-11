#-*-encoding:utf-8 -*-
#Models for Comision

from django.db import models

class Comision(models.Model):
	numero = models.CharField(max_length=100, default='',  verbose_name="Nº Comisión")
	turno = models.CharField(max_length=100, default='',  verbose_name="Turno") 
	nivel = models.CharField(max_length=2) 
	carrera = models.ForeignKey('carrera.Carrera') 
	
	
	def __unicode__(self):
		return '%s - %s - %s ' % (self.numero, self.turno, self.carrera.nombre)
