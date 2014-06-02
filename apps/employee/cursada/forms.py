#Forms for Cursada

from django.forms import ModelForm
from cursada.models import Cursada

class CursadaForm(ModelForm):
	class Meta:
		model = Cursada 

