#Project URLS

from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', include('apps.users.urls', namespace='users')),
	url(r'^admin/', include(admin.site.urls)),
	#URLS PER APP
	url(r'^alumnos/', include('apps.main_alumno.urls', namespace='alumnos')),
	url(r'^carreras/', include('apps.carrera.urls',namespace='carreras')),
	url(r'^catedras/', include('apps.catedra.urls', namespace='catedras')),
	url(r'^comisiones/', include('apps.comision.urls', namespace='comisiones')),
	url(r'^horarios/', include('apps.horario.urls', namespace='horarios')), 
	
)
