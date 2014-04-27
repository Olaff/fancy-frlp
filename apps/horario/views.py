#Views for Horario
from django.shortcuts import get_object_or_404,render,render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required, permission_required
from django.forms.models import inlineformset_factory
from django.contrib import messages
from carrera.models import Horario
from catedra.models import Catedra
from carrera.forms import HorarioForm


@permission_required('empleados.can_add')
def add_horario(request, id_catedra): #Recibe el id de catedra que agregue
	catedra = get_object_or_404(Catedra, pk=id_catedra) #Agarro la catedra 
	queryset = Comision.objects.filter(carrera = catedra.carrera, nivel=catedra.nivel)
	formlist_size = len(queryset)
	HorarioInlineFormSet = inlineformset_factory(Catedra, Horario, form=HorarioForm, max_num=formlist_size, can_delete=False) #Creo el inlineformset con los dos modelos
	HorarioInlineFormSet.form.base_fields["comision"].queryset = queryset
	if request.method =='POST':
		formset = HorarioInlineFormSet(request.POST, request.FILES, instance=catedra) #Instancio el formset con la catedra que agarre
		if formset.is_valid(): 
			#Si todo esta validado guardo en DB
			formset.save()
			#Envio un mensaje al usuario 
			messages.success(request,' Datos agregados exitosamente')
			#redirecciono a la lista de comisiones
			url = reverse ('catedra_list', args=[catedra.carrera]) #Redirijo a la lista de catedras segun la carrera
			return HttpResponseRedirect(url)
	else:
		formset = HorarioInlineFormSet(instance=catedra)
		
	template_vars = {'formset': formset} #Variable que le paso al contexto
	return render_to_response('add_horario.html', template_vars, context_instance=RequestContext(request))