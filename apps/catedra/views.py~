# Catedra VIEWS
# -*-encoding:utf-8-*-

from django.shortcuts import get_object_or_404,render,render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from catedra.models import Catedra
from catedra.forms import CatedraForm

@login_required(login_url='/login/')
def ListaCatedras(request, carrera): #Lista todas las cátedras recibiendo  como parámetro el nombre de la carrera para poder generar la lista
	catedras = Catedra.objects.filter(carrera__nombre__contains=carrera)
	template_vars = {'catedras':catedras}
	return render_to_response('catedra_list.html', template_vars, context_instance=RequestContext(request))
	

@login_required(login_url='/login/')	
def  CatedraDetails(request, id): #Devuelve el detalle de la cátedra seleccionada
	catedra = get_object_or_404(Catedra, pk=id)
	return render_to_response('catedra_details.html', {'catedra':catedra}, context_instance=RequestContext(request))
	#queryset = Catedra.objects.filter(carrera__nombre__contains='sistemas') 
	
# VISTAS PARA  GESTION DE CATEDRAS

@permission_required('empleados.can_add', raise_exception=True)
@login_required(login_url='/login/')
def add_catedra(request):
	form = CatedraForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		new_catedra = form.save()
		messages.success(request,' La catedra fue agregada exitosamente')
		return HttpResponseRedirect(reverse('catedras:catedra_details', args=[new_catedra.id])) #Redirecciona a la vista para agregar los horarios
	template_vars = {'form': form}
	return render_to_response('add_catedra.html', template_vars, context_instance=RequestContext(request))
	
@permission_required('empleados.can_edit', raise_exception=True)	
@login_required(login_url='/login/')
def edit_catedra(request, id):
	instance = get_object_or_404(Catedra, id=id)
	form = CatedraForm(request.POST or None , request.FILES or None , instance=instance)
	if form.is_valid():
			form.save()
			messages.success(request,'Catedra modificada satisfactoriamente')
			carrera = instance.carrera
			url = reverse('/catedras/catedra_list', args=[carrera])
			return HttpResponseRedirect(url)
					
	template_vars = {'form': form}
	return render_to_response('edit_catedra.html', template_vars, context_instance=RequestContext(request)) 

@permission_required('empleados.can_delete', raise_exception=True)	
def delete_catedra(request,id):
	catedra = get_object_or_404(Catedra, id=id)
	carrera = catedra.carrera
	catedra.delete()
	messages.success(request,'Catedra eliminada con éxito')
	url = reverse('catedras:catedra_list' ,args=[carrera])
	return HttpResponseRedirect(url)
