#URLS for Carrera
from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.carrera.models import Carrera
admin.autodiscover()

urlpatterns = patterns('carrera.views',
	url(r'^index_carrera/$', 'index_carrera', name='index_carrera'),
	url(r'^addcarrera/$','add_carrera', name='add_carrera'),
	url(r'^editar/(?P<id>\d+)/$', 'edit_carrera', name='edit_carrera'),
	url(r'^lista_carreras/$', 'carrera_list', name='carrera_list'),
	url(r'^(?P<id>\d+)/detalles/$', 'carrera_details', name='carrera_details'),
)
