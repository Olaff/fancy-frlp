#Views for Horario
# -*-encoding:utf-8-*-
from django.shortcuts import get_object_or_404,render,render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required, permission_required
from django.forms.models import inlineformset_factory
from django.contrib import messages
from horario.models import Horario
from catedra.models import Catedra
from comision.models import Comision
from horario.forms import HorarioForm


@permission_required('empleados.can_add', raise_exception = True)
def add_horario(request, id_catedra): #Recibe el id de catedra que agregue
	catedra = get_object_or_404(Catedra, pk=id_catedra) #Agarro la catedra 
	queryset = Comision.objects.filter(carrera = catedra.carrera, nivel=catedra.nivel)
	formlist_size = len(queryset)
	HorarioInlineFormSet = inlineformset_factory(Catedra, Horario,  form=HorarioForm, max_num=formlist_size, can_delete=False) #Creo el inlineformset con los dos modelos
	HorarioInlineFormSet.form.base_fields["comision"].queryset = queryset
	formset = HorarioInlineFormSet(request.POST or None , request.FILES or None , instance=catedra) #Instancio el formset con la catedra que agarre
	if formset.is_valid(): 
		#Si todo esta validado guardo en DB
		formset.save()
		#Envio un mensaje al usuario 
		messages.success(request,' Datos agregados exitosamente')
		#redirecciono a la lista de 
		url = reverse ('catedras:catedra_details', args=[catedra.id]) 
		return HttpResponseRedirect(url)
	template_vars = {'formset': formset, 'catedra': catedra} #Variable que le paso al contexto
	return render_to_response('add_horario.html', template_vars, context_instance=RequestContext(request))

#THIS IS NOT VERY DRY, FIX WHEN THE TIME COMES 
@permission_required('empleados.can_add', raise_exception = True)
def edit_horario(request, id_catedra, id_schedule): #Recibe el id de catedra que agregue
	form_num = id_schedule
	catedra = get_object_or_404(Catedra, pk=id_catedra) #Agarro la catedra 
	queryset = Comision.objects.filter(carrera = catedra.carrera, nivel=catedra.nivel)
	formlist_size = len(queryset)
	HorarioInlineFormSet = inlineformset_factory(Catedra, Horario,  form=HorarioForm, max_num=formlist_size, can_delete=False) #Creo el inlineformset con los dos modelos
	HorarioInlineFormSet.form.base_fields["comision"].queryset = queryset
	formset = HorarioInlineFormSet(request.POST or None , request.FILES or None , instance=catedra) #Instancio el formset con la catedra que agarre
	if formset.is_valid(): 
		#Si todo esta validado guardo en DB
		formset.save()
		#Envio un mensaje al usuario 
		messages.success(request,' Datos agregados exitosamente')
		#redirecciono a la lista de 
		url = reverse ('catedras:catedra_details', args=[catedra.id]) 
		return HttpResponseRedirect(url)
	template_vars = {'formset': formset, 'form_num': form_num, 'catedra': catedra } #Variable que le paso al contexto
	return render_to_response('edit_horario.html', template_vars, context_instance=RequestContext(request))

@permission_required('empleados.can_delete', raise_exception = True)
def delete_horario(request, id_catedra, id_schedule):
	pass
