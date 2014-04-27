#FORMS for Catedra
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import FormActions
from catedra.models import Catedra

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
					'sitio',
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