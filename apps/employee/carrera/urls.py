#URLS for Carrera
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('employee.carrera.views',
	url(r'^addcarrera/$','add_carrera', name='add_carrera'),
	url(r'^editar/(?P<slug>[-\w]+)/$', 'edit_carrera', name='edit_carrera'),
	url(r'^lista_carreras/$', 'carrera_list', name='carrera_list'),
	url(r'^(?P<slug>[-\w]+)/detalles/$', 'carrera_details', name='carrera_details'),
)
