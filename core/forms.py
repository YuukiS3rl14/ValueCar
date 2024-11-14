from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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

class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = ['supermercado','nombre','marca','precio','descripcion','origen_url','imagen_url','fecha_actualizacion']

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']