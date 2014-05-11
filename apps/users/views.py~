# -*- coding: utf-8 -*-
#Views for user handling

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,render,render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.views import login 
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.template.context import RequestContext
from apps.carrera.models import Carrera
from apps.comision.models import Comision 

@login_required(login_url='/login/')
def index(request):
	carreras = Carrera.objects.all()
	comisiones = Comision.objects.all()
	template_vars = {'carreras': carreras, 'comisiones': comisiones}
	return render_to_response('index.html', template_vars, context_instance=RequestContext(request))
	
#VISTAS PARA LOGOUT 
@login_required(login_url='/login/')
def logout_user(request):
	logout(request)
	messages.success(request,'Has cerrado sesión')
	return HttpResponseRedirect('/login/')
