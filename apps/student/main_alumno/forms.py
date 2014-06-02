#-*-encoding:utf-8 -*-
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import FormActions
from student.main_alumno.models import *
	         		
class AlumnoForm(ModelForm):
	class Meta:
		model = Alumno
		input_formats=['%d/%m/%Y'] 		
		exclude = ["slug"]
	
	def __init__(self, *args, **kwargs): #Reimplemento el constructor 
        	super(AlumnoForm, self).__init__(*args, **kwargs) #Llamo al padre
		# Customizo mensaje de error para todos los campos del formulario 
        	for field in self.fields.values():
           		field.error_messages = {'required':'Este campo es obligatorio'.format(fieldname=field.label)}
           	self.helper = FormHelper(self)
           	self.helper.form_class = 'form-horizontal'
           	self.helper.label_class = 'col-lg-3'
		self.helper.field_class = 'col-lg-5'
		self.helper.help_inline = True
		self.helper.layout = Layout (
			Fieldset(
				'Ingrese los datos del alumno',
				Div(
					Field('apellido', label="Apellido", placeholder="Apellido"),
					Field('nombres', label="Nombres"),
					Field('dni', label="Documento", placeholder="Ingrese sin puntos"),
					'fecha_nacimiento',
					'lugar',
					Field('domicilio', placeholder="Domicilio actual"),
					
					css_class='col-lg-6',
				),
				Div(					
					Field('localidad', placeholder="Localidad actual"),
					Field('telefono',placeholder="Ingrese sin guiones"),
					Field('celular', placeholder="Ingrese sin guiones"),
					Field('mail', placeholder="ejemplo@ejemplo.dominio"),
					'carrera',
					'legajo',
					css_class='col-sm-6',
				),
				FormActions(
    					Submit('submit', 'Guardar'),
    					HTML('<input type="reset" class="btn" name="reset" value="Borrar"/>'),
    					HTML("""<a class="btn btn-default" href="{% url 'users:employee_index' %}">Cancelar</a>"""),
    					css_class = 'pull-right',
			),
			),
			
		)


	
