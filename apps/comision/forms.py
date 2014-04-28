#FORMS for Comision
# -*-encoding:utf-8-*-

from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import FormActions
from comision.models import Comision

class ComisionForm(ModelForm):
	class Meta:
		model = Comision 
		
	def __init__(self, *args, **kwargs): #Reimplemento el constructor 
        	super(ComisionForm, self).__init__(*args, **kwargs) #Llamo al padre
		# Customizo mensaje de error para todos los campos del formulario 
        	for field in self.fields.values():
           		field.error_messages = {'required':'Este campo es obligatorio'.format(fieldname=field.label)}
           	self.helper = FormHelper(self)
           	self.helper.form_class = 'form-horizontal'
           	self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-4'
		self.helper.help_inline = True
           	self.helper.layout= Layout (
           		Fieldset(
           			'Ingrese una nueva comision',
           			Field('numero', label='Número', placeholder='Ingrese el numero de la comisión'),
           			Field('nivel', label='Nivel', placeholder='Ingrese el nivel al que pertenece comisión'),
           			Field('turno', label='Turno', placeholder='Ingrese el turno de la comisión'),
           			Field('carrera', label='Carrera', placeholder='Elija una carrera'),
           			
           		),
           		
           	        FormActions(
    				Submit('submit', 'Guardar'),
    				HTML('<input type="reset" class="btn" name="reset" value="Borrar"/>'),
    				HTML("""<a class="btn btn-default" href="{% url 'users:index' %}">Cancelar</a>"""),
    				css_class = 'pull-right',
			),
		)
