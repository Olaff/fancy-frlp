#URLS PARA GESTION DE ALUMNOS 
from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.main_alumno.models import Alumno
admin.autodiscover()

urlpatterns = patterns ('main_alumno.views',
	url(r'^addalumno/$', 'add_alumno', name='add_alumno'),
	url(r'^alumno/editar/(?P<id>\d+)/$', 'edit_alumno', name='alumno_edit'),
	url(r'^alumnos/$',  'ListaAlumnos', name='lista_alumnos'),
	url(r'^alumnos/(?P<id>\d+)/detalles/$', 'alumno_details', name='alumno_details'),
	url(r'^carrera/(?P<career>\w+)/$', 'alumno_by_career', name='alumno_by_career'),
)