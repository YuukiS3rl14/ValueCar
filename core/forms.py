from django import forms
from django.forms import ModelForm
from .models import *

# Template para poder usar el formulario en HTML

class UsuarioForm(ModelForm):

    class Meta:
        model = Usuario
        fields = ['rol','nombre','apellido','email','contraseña']

class RolForm(ModelForm):

    class Meta:
        model = Rol
        fields = ['nombre']