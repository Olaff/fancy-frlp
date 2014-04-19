from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login 
from main_alumno.forms import LoginForm
from main_alumno.models import Catedra,Carrera
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'main_alumno.views.index', name='index'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^login/$', login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
	url(r'^logout/$', 'main_alumno.views.logout_user', name='logout'),
	#URLS PARA GESTION DE CATEDRAS 
	url(r'^catedra/addcatedra/$', 'main_alumno.views.add_catedra', name='add_catedra'),
	url(r'^catedra/editar/(?P<id>\d+)/$', 'main_alumno.views.edit_catedra', name='catedra_edit'),
	url(r'^catedra/eliminar/(?P<id>\d+)/$', 'main_alumno.views.delete_catedra', name='catedra_delete'),
	url(r'^catedra/lista_catedras/(?P<carrera>\w+)/$', 'main_alumno.views.ListaCatedras', name='catedra_list'),
	url(r'^catedra/(?P<id>\d+)/detalles/$', 'main_alumno.views.CatedraDetails', name='catedra_details'),
	#URLS PARA HORARIOS
	url(r'^catedra/(?P<id_catedra>\d+)/addhorario/$', 'main_alumno.views.add_horario', name='add_horario'),
	url(r'^catedra/(?P<id_catedra>\d+)/edithorario/$', 'main_alumno.views.add_horario', name='edit_horario'),	
	#URLS PARA GESTION DE COMISIONES
	url(r'^comision/addcomision/$', 'main_alumno.views.add_comision', name='add_comision'),
	url(r'^comision/editar/(?P<id>\d+)/$', 'main_alumno.views.edit_comision', name='comision_edit'),
	url(r'^comision/lista_comisiones/$', 'main_alumno.views.comision_list', name='comision_list'),
	#URLS PARA GESTION DE ALUMNOS 
	url(r'^addalumno/$', 'main_alumno.views.add_alumno', name='add_alumno'),
	url(r'^alumno/editar/(?P<id>\d+)/$', 'main_alumno.views.edit_alumno', name='alumno_edit'),
	url(r'^alumnos/$',  'main_alumno.views.ListaAlumnos', name='lista_alumnos'),
	url(r'^alumnos/(?P<id>\d+)/detalles/$', 'main_alumno.views.alumno_details', name='alumno_details'),
	#URLS PARA GESTION DE CARRERAS
	url(r'^addcarrera/$','main_alumno.views.add_carrera', name='add_carrera'),
	url(r'^carrera/editar/(?P<id>\d+)/$', 'main_alumno.views.edit_carrera', name='edit_carrera'),
	url(r'^carrera/lista_carreras', 'main_alumno.views.carrera_list', name='carrera_list'),
	url(r'^carrera/(?P<id>\d+)/detalles/$', 'main_alumno.views.carrera_details', name='carrera_details'),
	url(r'^carrera/(?P<career>\w+)/$', 'main_alumno.views.alumno_by_career', name='alumno_by_career'),
)
