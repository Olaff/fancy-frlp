from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login 
from main_alumno.forms import LoginForm

admin.autodiscover()

urlpatterns = patterns('main_alumno',
	url(r'^$', 'views.index', name='index'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^login/$', login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
	url(r'^logout/$', 'main_alumno.views.logout_user', name='logout'),
	#URLS PER APP
	url(r'^carreras/', include(carrera.urls,namespace='carrera')),
	url(r'^catedras/', include(catedra.urls, namespace='catedra')),
	url(r'^comisiones/', include(comision.urls, namespace='comision')),
	url(r'^horarios/', include(horario.urls, namespace='horario')), 
	#URLS PARA GESTION DE ALUMNOS 
	url(r'^addalumno/$', 'views.add_alumno', name='add_alumno'),
	url(r'^alumno/editar/(?P<id>\d+)/$', 'views.edit_alumno', name='alumno_edit'),
	url(r'^alumnos/$',  'ListaAlumnos', name='lista_alumnos'),
	url(r'^alumnos/(?P<id>\d+)/detalles/$', 'alumno_details', name='alumno_details'),
	url(r'^carrera/(?P<career>\w+)/$', 'alumno_by_career', name='alumno_by_career'),
)
