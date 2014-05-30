from django.conf import settings
from django.contrib.auth.models import check_password
from apps.users.models import GenericUser

class AuthBackend(object):
	'''
	Custom authentication backend. Allow users to log in using specified field
	'''
	class Meta:
		abstract = True
		
class EmailAuth(AuthBackend):
	def authenticate(self, email=None, password=None):
		try:
			user = GenericUser.objects.get(email=email)
			if user.check_password(password):
				return user
			
		except GenericUser.DoesNotExist:
			return None
	
	def get_user(self, user_id):
		try:
			user = GenericUser.objects.get(pk=user_id)
			if user.is_active:
				return user
			return None
		except GenericUser.DoesNotExist:
			return None

class LegajoAuth(AuthBackend):
	def get_user(self, user_id):
		try:
			user = GenericUser.objects.get(pk=user_id)
			if user.is_active:
				return user
			return None
		except GenericUser.DoesNotExist:
			return None
				
	def authenticate(self, legajo=None, password=None):
		try: 
			user = GenericUser.objects.get(legajo=legajo)
			if user.check_password(password):
				return user
		except GenericUser.DoesNotExist:
			return None
	
