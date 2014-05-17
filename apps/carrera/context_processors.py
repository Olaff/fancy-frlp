# Custom context_processor for carrera 
from apps.carrera.models import Carrera 

def get_carreras(request):
	carreras = Carrera.objects.all()
	template_vars = {'carreras': carreras}
	return template_vars
