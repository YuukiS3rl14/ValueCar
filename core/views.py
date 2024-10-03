from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

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

def mostraradmin(request):
    return render(request, 'core/admin.html')



