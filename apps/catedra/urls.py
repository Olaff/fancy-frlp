#URLS for Catedra
from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.catedra.models import Catedra
admin.autodiscover()

urlpatterns = patterns('catedra.views',
	url(r'^addcatedra/$', 'add_catedra', name='add_catedra'),
	url(r'^editar/(?P<slug>[-\w]+)/$', 'edit_catedra', name='catedra_edit'),
	url(r'^eliminar/(?P<slug>[-\w]+)/$', 'delete_catedra', name='catedra_delete'),
	url(r'^lista_catedras/(?P<carrera>\w+)/$', 'ListaCatedras', name='catedra_list'),
	url(r'^(?P<slug>[-\w]+)/detalles/$', 'CatedraDetails', name='catedra_details'),
)
