#URLS for user handling
from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.users.views',
	url(r'^$', 'index', name="index"),
	url(r'^login$', 'login', name='login'),
#	url(r'^student/login$', 'student_login', name='student_login'),	
	url(r'^logout$', 'logout', name='logout'),
	
)
