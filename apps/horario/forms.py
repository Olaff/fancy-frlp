#Forms for Horario
# -*-encoding:utf-8-*-
from django.db import models
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import FormActions
from horario.models import Horario

class HorarioForm(ModelForm):
	class Meta:
         	model = Horario
         	
	def __init__(self, *args, **kwargs): #Reimplemento el constructor 
        	super(HorarioForm, self).__init__(*args, **kwargs) #Llamo al padre
		# Customizo mensaje de error para todos los campos del formulario 
		for field in self.fields.values():
        		field.error_messages = {'required':'Este campo es obligatorio'.format(fieldname=field.label), 'invalid': "No es un formato válido, vieja."}
        		 
           	self.helper = FormHelper(self)
           	self.helper.form_class = 'form-horizontal'
           	self.helper.label_class = 'col-lg-3'
		self.helper.field_class = 'col-lg-4'
		self.helper.help_inline = True
		self.helper.layout= Layout (
           		Fieldset(
           			'Ingrese el detalle para la catedra seleccionada',
           			Field('comision', label='Comisión'),
           			Fieldset(
           				'Info clase teorica',
           				Field('prof_t', label='Prof. Teoria', placeholder='Nombre y apellido'),
           				'dia_t',
           				'hora_inicio_t',
           				'hora_fin_t',
           				css_class='col-lg-6',
           			),
           			Fieldset(
           				'Info clase practica',
           				Field('prof_p', label='Prof.  Practica', placeholder='Nombre y apellido'),
           				'dia_p',
           				'hora_inicio_p',
           				'hora_fin_p',
           				
           				css_class='col-lg-6'
           			),
           			Field('ayudantes', label='Ayudantes', placeholder='ayudantes'),
           			          			
           		),
           		FormActions(
    					HTML('<input type="submit" class="btn btn-primary"name="submit" value="Guardar"/>'),           		
           		),
           	)
           	        	
		
