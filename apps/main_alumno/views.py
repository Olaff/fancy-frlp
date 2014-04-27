#-*-encoding:utf-8
# Views for Alumno 
from apps.main_alumno.models import Alumno
from apps.main_alumno.forms import AlumnoForm
from apps.main_alumno.tables import AlumnoTable
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,render,render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.template.context import RequestContext
from django_tables2   import RequestConfig
from apps.carrera.models import Carrera
from apps.comision.models import Comision
             		  
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
def ListaAlumnos(request):
	alumnos = Alumno.objects.all()
	return render_to_response('alumno_list.html', {'alumnos': alumnos}, context_instance=RequestContext(request))
	
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
	
