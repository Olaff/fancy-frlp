# -*-encoding:utf-8-*-
#FORMS FOR CARRERA

from django.forms import ModelForm
from carrera.models  import Carrera
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import FormActions
from main_alumno.models import *

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
    				HTML('<input type="submit" class="btn btn-inverse" name="submit" value="Guardar"/>'),
    				HTML('<input type="reset" class="btn btn-default" name="reset" value="Borrar"/>'),
    				HTML("""<a class="btn btn-default" href="{% url 'users:index' %}">Cancelar</a>"""),
    				css_class = 'pull-right',
			),
		)
	
	class Meta:
		model = Carrera
		exclude= ["slug"]
