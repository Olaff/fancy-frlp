#URLS for Horario
from django.conf.urls import patterns, include, url
from django.contrib import admin
from carrera.models import Horario
admin.autodiscover()

urlpatterns = patterns('carrera.views',
	url(r'^catedra/(?P<id_catedra>\d+)/addhorario/$', 'main_alumno.views.add_horario', name='add_horario'),
	url(r'^catedra/(?P<id_catedra>\d+)/edithorario/$', 'main_alumno.views.add_horario', name='edit_horario'),
)	
