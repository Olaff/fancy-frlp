#VIEWS FOR CARRERA
from django.shortcuts import get_object_or_404,render,render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from carrera.models import Carrera
from carrera.forms import CarreraForm

def add_carrera(request):
	if request.method =='POST':
		form = CarreraForm(request.POST)
		if form.is_valid():
			new_carrera = form.save()
			messages.success(request,'Carrera agregada satisfactoriamente')
			return HttpResponseRedirect('/carrera/lista_carreras')
	else:
		form = CarreraForm
	
	template_vars = {'form':form}
	return render_to_response('add_carrera.html', template_vars, context_instance=RequestContext(request))
	
def edit_carrera(request, id):
	instance = get_object_or_404(Carrera, id=id)
	form = CarreraForm(request.POST or None , instance=instance)
	if form.is_valid():
			form.save()
			messages.success(request,'Datos de la carrera modificados satisfactoriamente')
			return HttpResponseRedirect('/carrera/lista_carreras')
					
	template_vars = {'form': form}
	return render_to_response('add_carrera.html', template_vars, context_instance=RequestContext(request))
	 
def carrera_list(request):
	carreras = Carrera.objects.all()
	template_vars = {'carreras': carreras}
	return render_to_response('carrera_list.html', template_vars, context_instance=RequestContext(request))

@login_required(login_url='/login/')	
def carrera_details(request, id):
	carrera = get_object_or_404(Carrera, id=id)
	return render_to_response('carrera_details.html', {'carrera':carrera}, context_instance=RequestContext(request))