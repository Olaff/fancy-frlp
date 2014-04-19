#-*-encoding:utf-8
from main_alumno.models import *
from main_alumno.forms import *
from main_alumno.tables import AlumnoTable
from django.forms.models import modelformset_factory, inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,render,render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import login 
from django.contrib import messages
from django.template.context import RequestContext
from django_tables2   import RequestConfig
             		  
@login_required(login_url='/login/')
def index(request):
	carreras = Carrera.objects.all()
	comisiones = Comision.objects.all()
	template_vars = {'carreras': carreras, 'comisiones': comisiones}
	return render_to_response('index.html', template_vars, context_instance=RequestContext(request))
	
#VISTAS PARA LOGOUT 
def logout_user(request):
	logout(request)
	messages.success(request,'Has cerrado sesión')
	return HttpResponseRedirect('/login/')
	

# VISTAS PARA LISTADO

@login_required(login_url='/login/')
def ListaAlumnos(request):
	alumnos = Alumno.objects.all()
	return render_to_response('alumno_list.html', {'alumnos': alumnos}, context_instance=RequestContext(request))
	
@login_required(login_url='/login/')	
def ListaCatedras(request, carrera): #Lista todas las cátedras recibiendo  como parámetro el nombre de la carrera para poder generar la lista
	catedras = Catedra.objects.filter(carrera__nombre__contains=carrera)
	template_vars = {'catedras':catedras}
	return render_to_response('catedra_list.html', template_vars, context_instance=RequestContext(request))
	

@login_required(login_url='/login/')	
def  CatedraDetails(request, id): #Devuelve el detalle de la cátedra seleccionada
	catedra = get_object_or_404(Catedra, pk=id)
	horario = Horario.objects.filter()
	return render_to_response('catedra_details.html', {'catedra':catedra}, context_instance=RequestContext(request))
	#queryset = Catedra.objects.filter(carrera__nombre__contains='sistemas') 
	
# VISTAS PARA  GESTION DE CATEDRAS

@permission_required('empleados.can_add')
@login_required(login_url='/login/')
def add_catedra(request):
	if request.method =='POST':
		form = CatedraForm(request.POST, request.FILES)
		if form.is_valid():
			new_catedra = form.save()
			messages.success(request,' La catedra fue agregada exitosamente')
			return HttpResponseRedirect(reverse('catedra_details', args=[new_catedra.id])) #Redirecciona a la vista para agregar los horarios
	else:
		form = CatedraForm
		
	template_vars = {'form': form}
	return render_to_response('add_catedra.html', template_vars, context_instance=RequestContext(request))
	
@permission_required('empleados.can_edit')	
@login_required(login_url='/login/')
def edit_catedra(request, id):
	instance = get_object_or_404(Catedra, id=id)
	form = CatedraForm(request.POST or None , request.FILES, instance=instance)
	if form.is_valid():
			form.save()
			messages.success(request,'Catedra modificada satisfactoriamente')
			carrera = instance.carrera
			url = reverse('catedra_list')
			return HttpResponseRedirect(url)
					
	template_vars = {'form': form}
	return render_to_response('edit_catedra.html', template_vars, context_instance=RequestContext(request)) 

@permission_required('empleados.can_delete')	
def delete_catedra(request,id):
	catedra = get_object_or_404(Catedra, id=id)
	carrera = catedra.carrera
	catedra.delete()
	messages.success(request,'Catedra eliminada con éxito')
	url = reverse('catedra_list' ,args=[carrera])
	return HttpResponseRedirect(url)
	
	
#GESTION DE HORARIOS
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
	
#GESTION DE COMISIONES

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
			url = reverse ('comision_list')
			return HttpResponseRedirect(url)
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
def comision_list(request): #Lista todas las comisiones, por ahora
	comisiones = Comision.objects.all()
	template_vars = {'comisiones':comisiones}
	return render_to_response('comision_list.html', template_vars, context_instance=RequestContext(request))
	
#GESTION DE ALUMNOS
@login_required(login_url='/login/')	
def add_alumno(request):
	if request.method =='POST':
		form = AlumnoForm(request.POST)
		if form.is_valid():
			new_alumno = form.save()
			messages.success(request, 'Alumno añadido satisfactoriamente')
			return HttpResponseRedirect('/alumnos')
	else:
		form = AlumnoForm()
	
	template_vars = {'form': form}
	return render_to_response('agregaralumno.html', template_vars, context_instance=RequestContext(request))
	
@login_required(login_url='/login/')
def edit_alumno(request, id):
	instance = get_object_or_404(Alumno, id=id)
	form = AlumnoForm(request.POST or None , instance=instance)
	if form.is_valid():
			form.save()
			messages.success(request,'Datos del alumno modificados satisfactoriamente')
			return HttpResponseRedirect('/index')
					
	template_vars = {'form': form}
	return render_to_response('edit_alumno.html', template_vars, context_instance=RequestContext(request)) 
	
@login_required(login_url='/login/')
def alumno_by_career(request, career):
	#Para instanciar la tabla necesito un queryset
	alumnos = AlumnoTable(Alumno.objects.filter(carrera__nombre__contains=career))
	#Para paginar
	alumnos.paginate(page=request.GET.get('page', 1), per_page=2)
    	RequestConfig(request).configure(alumnos)
	template_vars = {'alumnos': alumnos}
	return render_to_response ('alumno_by_career.html', template_vars, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def alumno_details(request,id):
	alumno = get_object_or_404(Alumno, id=id)
	return render_to_response ('alumno_details.html', {'alumno': alumno}, context_instance=RequestContext(request))
	
# GESTION DE CARRERAS
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
