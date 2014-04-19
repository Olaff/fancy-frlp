#-*-encoding:utf-8 -*-
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import FormActions
from main_alumno.models import *

class LoginForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
        	super(LoginForm, self).__init__(*args, **kwargs)
        	self.fields['username'].label = "Usuario"
        	self.fields['password'].label = "Contraseña"
        	for field in self.fields.values():
           		field.error_messages = {'required':'Este campo es obligatorio'.format(fieldname=field.label)}
        	self.helper = FormHelper(self)
        	self.helper.layout = Layout(
            		Field('username', label="Usuario", placeholder="Nombre de usuario"),
            		Field('password', placeholder="Contraseña"),
        	)
	
class CatedraForm(ModelForm):
	def __init__(self, *args, **kwargs): #Reimplemento el constructor 
        	super(CatedraForm, self).__init__(*args, **kwargs) #Llamo al padre
		# Customizo mensaje de error para todos los campos del formulario 
        	for field in self.fields.values():
           		field.error_messages = {'required':'Este campo es obligatorio'.format(fieldname=field.label)}
           	#CrispyForms
           	self.helper = FormHelper(self)
           	self.helper.form_class = 'form-horizontal'
           	self.helper.label_class = 'col-sm-2'
		self.helper.field_class = 'col-lg-4'
		self.helper.help_inline = True
		self.helper.layout = Layout(
			Fieldset(
					'Ingrese los datos de la catedra',
					'nombre',
					'carrera',
					'nivel',
					'electiva',
					'sylabus',
					'jefe_catedra',
					'jtp',
			),
			FormActions(
    					Submit('submit', 'Guardar'),
    					HTML('<input type="reset" name="reset" value="Borrar"/>'),
    					HTML("""<a class="btn btn-default" href="{% url 'index' %}">Cancelar</a>"""),
    					css_class = 'pull-right',
			),
		)
           	
           	
	class Meta:
		model = Catedra #Conecta los campos del modelo para generar los del formulario
		exclude = ["slug", "comisiones"]	 #Excluyo comisiones porque la relacion se guarda en la vista del formset 	
	
	
           	
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
    				HTML("""<a class="btn btn-default" href="{% url 'index' %}">Cancelar</a>"""),
    				css_class = 'pull-right',
			),
		)

class HorarioForm(ModelForm):
	class Meta:
         	model = Horario
         	
	def __init__(self, *args, **kwargs): #Reimplemento el constructor 
        	super(HorarioForm, self).__init__(*args, **kwargs) #Llamo al padre
		# Customizo mensaje de error para todos los campos del formulario 
		for field in self.fields.values():
        		field.error_messages = {'required':'Este campo es obligatorio'.format(fieldname=field.label)}
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
           	)
           	
		self.helper.add_input(Submit('submit', 'Guardar'))
			
           		
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
    					HTML("""<a class="btn btn-default" href="{% url 'index' %}">Cancelar</a>"""),
    					css_class = 'pull-right',
			),
			),
			
		)

class CarreraForm(ModelForm):
	def __init__(self, *args, **kwargs): #Reimplemento el constructor 
        	super(CarreraForm, self).__init__(*args, **kwargs) #Llamo al padre
		# Customizo mensaje de error para todos los campos del formulario 
        	for field in self.fields.values():
           		field.error_messages = {'required':'Este campo obligatorio'.format(fieldname=field.label)}
		#CrispyForms
		self.helper = FormHelper(self)
           	self.helper.form_class = 'form-horizontal'
           	self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-4'
		self.helper.help_inline = True
           	self.helper.layout= Layout (
           		Fieldset(
           			'Ingrese una nueva carrera',
           			'nombre',
           			'tit_intermedio',
           			'planestudio',
           			Field('year', label='Año', placeholder='Año del plan de estudios'),
           		),
           		
           	        FormActions(
    				Submit('submit', 'Guardar'),
    				HTML('<input type="reset" class="btn" name="reset" value="Borrar"/>'),
    				HTML("""<a class="btn btn-default" href="{% url 'index' %}">Cancelar</a>"""),
    				css_class = 'pull-right',
			),
		)
	
	class Meta:
		model = Carrera
		exclude= ["slug"]
	
