#URLS for Comision
from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.comision.models import Comision
admin.autodiscover()

urlpatterns = patterns('comision.views',
	url(r'^addcomision/$', 'add_comision', name='add_comision'),
	url(r'^editar/(?P<id>\d+)/$', 'edit_comision', name='comision_edit'),
	url(r'^eliminar/(?P<id>\d+)/$', 'comision_delete', name='comision_delete'),
	url(r'^lista_comisiones/$', 'comision_list', name='comision_list'),
	url(r'^(?P<id>\d+)/detalles/$', 'comision_detail', name='comision_detail'),
)
