#-*-encoding:utf-8 -*-
# FORMS for USERS 
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *

class LoginForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
        	super(LoginForm, self).__init__(*args, **kwargs)
        	self.fields['username'].label = "Usuario"
        	self.fields['password'].label = "Contraseña"
        	for field in self.fields.values():
           		field.error_messages = {'required':'Este campo es obligatorio'.format(fieldname=field.label)}
        	
