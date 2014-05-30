# -*- coding: utf-8 -*-
#Views for user handling

from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from apps.users.forms import EmployeeAuthenticationForm, StudentAuthenticationForm

def employee_login(request):
	'''
	Log in view
	'''
	employee_form = EmployeeAuthenticationForm(request.POST or None)
	if employee_form.is_valid():
		user = authenticate(email=request.POST['email'], password=request.POST['password'])
		if user is not None:
			if user.is_active:
				django_login(request, user)
				return redirect('users:employee_index')
	template_vars = {'employee_form': employee_form}
	return render_to_response('employee_login.html', template_vars, context_instance=RequestContext(request))

def student_login(request):
	'''
	Log in view
	'''
	student_form = StudentAuthenticationForm(request.POST or None)
	if student_form.is_valid():
		user = authenticate(legajo=request.POST['legajo'], password=request.POST['password'])
		if user is not None:
			if user.is_active:
				django_login(request, user)
				return redirect('users:employee_index')
	template_vars = {'student_form': student_form}
	return render_to_response('student_login.html', template_vars, context_instance=RequestContext(request))  

def logout(request):
    """
    Log out view
    """
    django_logout(request)
    return redirect('users:employee_login')
    
def landing(request):
	return render_to_response('landing_page.html', context_instance=RequestContext(request))


