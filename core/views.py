from django.shortcuts import render, redirect
from django.db.models import Q
from .models import *
from .forms import *

# Create your views here.

def showIndex(request):
    listproducts5 = Producto.objects.order_by('-fecha_actualizacion')[:5]
    listproducts10 = Producto.objects.order_by('precio')[:10]
    
    datos = {
        'products5': listproducts5,
        'products10': listproducts10
    }
    
    return render(request, 'core/index.html', datos)

def showLogin(request):
    return render(request, 'core/login.html')

def showRegister(request):
    return render(request, 'core/registro.html')

def showContact(request):
    return render(request, 'core/contactos.html')

def showSearch(request):
    query = request.POST.get('query', '')
    results = Producto.objects.filter(
        Q(nombre__icontains=query) | 
        Q(marca__icontains=query) | 
        Q(descripcion__icontains=query) | 
        Q(supermercado__nombre__icontains=query)
    )
    return render(request, 'core/search.html', {'results': results, 'query': query})

def showFavorite(request):
    return render(request, 'core/favoritos.html')

def showAboutUs(request):
    return render(request, 'core/aboutus.html')

def showAdmin(request):
    return render(request, 'core/admin.html')

def addProduct(request):

    datos = {'form': ProductoForm()}

    if request.method == 'POST':
        form = ProductoForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            datos['msj'] = 'Producto agregado correctamente'
        else:
            datos['msj'] = 'El producto no ha sido agregado'

    return render(request, 'core/Users/add.html', datos)

def listProduct(request):

    listproduct = Producto.objects.all()
    datos = {'product': listproduct}

    return render(request, 'core/Users/list.html', datos)

def updateProduct(request, id):

    product = Producto.objects.get(id=id)
    datos = {'form': ProductoForm(instance=product)}

    if request.method == 'POST':
        form = ProductoForm(data=request.POST, instance=product, files=request.FILES)
        if form.is_valid():
            form.save()
            datos['msj'] = 'Producto modificado correctamente'
            datos['form'] = form
        else:
            datos['msj'] = 'El producto no ha sido modificado'

    return render(request, 'core/Users/update.html', datos)

def deleteProduct(request, id):

    user = Producto.objects.get(id=id)
    user.delete()

    return redirect(to="list")





