#URLS PARA GESTION DE ALUMNOS 
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns ('student.main_alumno.views',
	url(r'^addalumno/$', 'add_alumno', name='add_alumno'),
	url(r'^alumnos/editar/(?P<id>\d+)/$', 'edit_alumno', name='edit_alumno'),
	url(r'^alumnos/eliminar/(?P<id>\d+)/$', 'delete_alumno', name='delete_alumno'),
	url(r'^alumnos/$',  'ListaAlumnos', name='lista_alumnos'),
	url(r'^alumnos/(?P<id>\d+)/detalles/$', 'alumno_details', name='alumno_details'),
	url(r'^alumnos/buscar/$', 'search_alumno', name="search_alumno"),
	url(r'^alumnos/buscar/results/$', 'search_results', name="search_results"),
	url(r'^carrera/(?P<career>\w+)/$', 'alumno_by_career', name='alumno_by_career'),
	
)
