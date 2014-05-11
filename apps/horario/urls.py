#URLS for Horario
from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.horario.models import Horario
admin.autodiscover()

urlpatterns = patterns('horario.views',
	url(r'^(?P<id_catedra>\d+)/addhorario/$', 'add_horario', name='add_horario'),
	url(r'^(?P<id_catedra>\d+)/edithorario/(?P<id_schedule>\d+)/$', 'edit_horario', name='edit_horario'),
)	
