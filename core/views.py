from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def mostrarindex(request):
    return render(request, 'core/index.html')

def mostrarlogin(request):
    return render(request, 'core/login.html')

def mostrarregistro(request):
    return render(request, 'core/registro.html')

def mostrarcontactos(request):
    return render(request, 'core/contactos.html')

def mostrarsearch(request):
    return render(request, 'core/search.html')

def mostrarfavoritos(request):
    return render(request, 'core/favoritos.html')

def mostraraboutus(request):
    return render(request, 'core/aboutus.html')

def mostraradmin(request):
    return render(request, 'core/admin.html')

def adduser(request):

    datos = {'form': UsuarioForm()}

    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            datos['msj'] = 'Usuario agregado correctamente'
        else:
            datos['msj'] = 'El usuario no ha sido agregado'

    return render(request, 'core/Users/add.html', datos)

def listuser(request):

    listuser = Usuario.objects.all()
    datos = {'users': listuser}

    return render(request, 'core/Users/list.html', datos)

def updateuser(request, id):

    user = Usuario.objects.get(id=id)
    datos = {'form': UsuarioForm(instance=user)}

    if request.method == 'POST':
        form = UsuarioForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            datos['msj'] = 'Usuario modificado correctamente'
            datos['form'] = form
        else:
            datos['msj'] = 'El usuario no ha sido modificado'

    return render(request, 'core/Users/add.html', datos)

def deleteuser(request, id):
    return render(request, 'core/Users/delete.html')





