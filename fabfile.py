#Fabric for management some magic stuff
from fabric.api import lcd, local

APPS_TO_WATCH = ['apps.main_alumno','apps.carrera','apps.catedra','apps.comision', 'apps.horario', 'apps.users']

def initial_migration():
    for app in APPS_TO_WATCH:
        local('python manage.py schemamigration %s --initial' % app)
        
def auto_migration():
    for app in APPS_TO_WATCH:
        local('python manage.py schemamigration %s --auto' % app)
        
def apply_migration():
    for app in APPS_TO_WATCH:
    	local('python manage.py migrate %s' %app)


