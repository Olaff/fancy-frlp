# -*- coding: utf-8 -*-
#Views for user handling

from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from apps.users.forms import EmployeeAuthenticationForm, StudentAuthenticationForm
from django.contrib import messages

#LANDING PAGE
def landing(request):
	return render_to_response('landing_page.html', context_instance=RequestContext(request))

#EMPLOYEE VIEWS

def employee_login(request):
	'''
	Employee Log in view
	'''
	form = EmployeeAuthenticationForm(request.POST or None)
	if form.is_valid():
		user = authenticate(email=request.POST['email'], password=request.POST['password'])
		if user is not None:
			if user.is_active:
				django_login(request, user)
				return redirect('users:employee_index')
	template_vars = {'form': form}
	return render_to_response('employee_login.html', template_vars, context_instance=RequestContext(request))
	
def employee_index(request):
	return render_to_response('employee_index.html', context_instance=RequestContext(request))

#STUDENT VIEWS 
def student_login(request):
	'''
	Student Log in view
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

def student_index(request):
	return render_to_response('student_index.html', context_instance=RequestContext(request))

def logout(request):
    """
    Log out view
    """
    django_logout(request)
    messages.success(request,'Has cerrado sesión')
    return redirect('/')
    



