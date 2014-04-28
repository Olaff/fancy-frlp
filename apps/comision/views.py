# -*-encoding:utf-8-*-

#Views for Comision
from django.shortcuts import get_object_or_404,render,render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.template.context import RequestContext
from django.contrib import messages
from comision.models import Comision
from comision.forms import ComisionForm

# VIEWS PARA GESTION DE COMISIONES

@login_required(login_url='/login/')
@permission_required('empleados.can_add') #Permisos de usuario
def add_comision(request):
	if request.method =='POST':
		form = ComisionForm(request.POST)
		if form.is_valid(): 
			#Si todo esta validado guardo en DB
			form.save()
			#Envio un mensaje al usuario 
			messages.success(request,' La comisión fue agregada exitosamente')
			#redirecciono a la lista de comisiones
			return HttpResponseRedirect('comisiones/comision_list')
	else:
		form= ComisionForm() #Para no mostrar las comisiones guardadas, uso objects.none()
		
	template_vars = {'form': form} #Variable que le paso al contexto
	return render_to_response('add_comision.html', template_vars, context_instance=RequestContext(request))
	
@permission_required('empleados.can_edit')
@login_required(login_url='/login/')
def edit_comision(request, id):
	instance = get_object_or_404(Comision, id=id)
	form = ComisionForm(request.POST or None , request.FILES, instance=instance)
	if form.is_valid():
			form.save()
			messages.success(request,'Comisión modificada satisfactoriamente')
			carrera = instance.carrera
			url = reverse('comision_list',args=[carrera])
			return HttpResponseRedirect(url)
					
	template_vars = {'form': form}
	return render_to_response('edit_comision.html', template_vars, context_instance=RequestContext(request)) 

@login_required(login_url='/login/')
def comision_delete(request, id):
	comision = get_object_or_404(Comision, id=id)
	comision.delete()
	messages.success(request,'Comision eliminada satisfactoriamente')
	return HttpResponseRedirect('comisiones/comision_list')
	
@login_required(login_url='/login/')	
def comision_list(request): #Lista todas las comisiones, por ahora
	comisiones = Comision.objects.all()
	template_vars = {'comisiones':comisiones}
	return render_to_response('comision_list.html', template_vars, context_instance=RequestContext(request))
	
@login_required(login_url='/login/')
def comision_detail(request, id):
	comision = get_object_or_404(Comision, id=id)
	return render_to_response ('comision_details.html', {'comision':comision}, context_instance=RequestContext(request))
	

