#URLS for user handling
from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login 
from apps.users.forms import LoginForm

urlpatterns = patterns('apps.users.views',
	url(r'^$', 'index', name='index'),
	url(r'^login/$', login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
	url(r'^logout/$', 'logout_user', name='logout_user'),
)
