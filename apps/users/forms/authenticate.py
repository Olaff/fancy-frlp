#-*-encoding:utf-8 -*-
# Authentication Form for Employee
from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import FormActions

class EmployeeAuthenticationForm(forms.Form):
	"""
	Login Form for Employee
	"""
	email = forms.EmailField(widget=forms.widgets.TextInput)
    	password = forms.CharField(widget=forms.widgets.PasswordInput)
    	
	class Meta:
        	fields = ['email', 'password']
        
        def __init__(self, *args, **kwargs): #Reimplemento el constructor 
        	super(EmployeeAuthenticationForm, self).__init__(*args, **kwargs) #Llamo al padre
		# Customizo mensaje de error para todos los campos del formulario 
        	for field in self.fields.values():
           		field.error_messages = {
           			'required':'Este campo obligatorio'.format(fieldname=field.label),
           		
           		}
		#CrispyForms
		self.helper = FormHelper(self)
		self.helper.layout = Layout(
			Fieldset(
				'Ingrese al sistema',
				Field('email', placeholder='Correo electrónico'),
				Field('password', label='Contraseña', placeholder='Contraseña'),
			),
			FormActions(
				Div (
					HTML('<input type="submit" class="btn  btn-default" name="submit" value="Entrar"/>'),
					HTML("""<a class="btn btn-info" href="#">Registrarse!</a>"""),
					css_class = 'pull-right'
				),				
			),
		)

class StudentAuthenticationForm(forms.Form):
	"""
	Login Form for Employee
	"""
	legajo= forms.IntegerField(widget=forms.widgets.TextInput)
    	password = forms.CharField(widget=forms.widgets.PasswordInput)
    	
	class Meta:
        	fields = ['legajo', 'password']
        
        def __init__(self, *args, **kwargs): #Reimplemento el constructor 
        	super(StudentAuthenticationForm, self).__init__(*args, **kwargs) #Llamo al padre
		# Customizo mensaje de error para todos los campos del formulario 
        	for field in self.fields.values():
           		field.error_messages = {
           			'required':'Este campo obligatorio'.format(fieldname=field.label),
           		
           		}
		#CrispyForms
		self.helper = FormHelper(self)
		
