#URLS for Comision
from django.conf.urls import patterns, include, url
from django.contrib import admin
from carrera.models import Comision
admin.autodiscover()

urlpatterns = patterns('comision.views',
	url(r'^comision/addcomision/$', 'add_comision', name='add_comision'),
	url(r'^comision/editar/(?P<id>\d+)/$', 'edit_comision', name='comision_edit'),
	url(r'^comision/lista_comisiones/$', 'comision_list', name='comision_list'),
)
