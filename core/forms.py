from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

# Template para poder usar el formulario en HTML

class RolForm(ModelForm):

    class Meta:
        model = Rol
        fields = ['nombre']

class AutoForm(ModelForm):

    class Meta:
        model = Auto
        fields = ['id', 'automotora', 'nombre', 'marca', 'modelo', 'año', 'precio','descripcion','imagen','origen','kilometraje','tipo_combustible','potencia','tipo_transmicion','color']

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ['titulo', 'texto', 'calificacion']

    usuario_id = forms.IntegerField(widget=forms.HiddenInput())
    auto_id = forms.IntegerField(widget=forms.HiddenInput())
