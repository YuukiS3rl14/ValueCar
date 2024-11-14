from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404

from .models import *
from .forms import *

# Create your views here.

def showIndex(request):
    listproducts5 = Producto.objects.order_by('-fecha_actualizacion')[:5]
    listproductslider = Producto.objects.filter(supermercado__nombre='Lider').order_by('precio')[:10]
    listproductsjumbo = Producto.objects.filter(supermercado__nombre='Jumbo').order_by('precio')[:10]
    listproductssanta_isabel = Producto.objects.filter(supermercado__nombre='Santa Isabel').order_by('precio')[:10]
    
    datos = {
        'products5': listproducts5,
        'productslider': listproductslider,
        'productsjumbo': listproductsjumbo,
        'productssanta_isabel': listproductssanta_isabel,
        'mostrar_filtros': True
    }
    
    return render(request, 'core/index.html', datos)

def showRegistro(request):
    data = {
        'form': RegistroForm()
        }
    
    if request.method == 'POST':
        form = RegistroForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username = form.cleaned_data["username"], password = form.cleaned_data["password1"])
            login(request, user)
            messages.success(request, 'Registro exitoso!')
            return redirect(to='index')
        data["form"] = form

    return render(request, 'registration/registro.html', data)

def showSearch(request):
    query = request.GET.get('query', '') 
    price_range = request.GET.get('price', '')
    category = request.GET.get('category', '')
    market = request.GET.get('market', '')
    name_initial = request.GET.get('name_initial', '')

    results = Producto.objects.all()

    if query:
        results = results.filter(
            Q(nombre__icontains=query) | 
            Q(marca__icontains=query) | 
            Q(descripcion__icontains=query) | 
            Q(supermercado__nombre__icontains=query)
        )

    if price_range:
        min_price, max_price = price_range.split('-')
        if max_price == '+':
            results = results.filter(precio__gte=min_price)  
        else:
            results = results.filter(precio__gte=min_price, precio__lte=max_price)  

    if category:
        results = results.filter(marca=category)
    if market:
        results = results.filter(supermercado=market)
    if name_initial:
        results = results.filter(nombre__istartswith=name_initial)

    return render(request, 'core/search.html', {'results': results, 'query': query, 'mostrar_filtros': True})

@login_required
def showFavorite(request):
    listproducts5 = Producto.objects.order_by('-fecha_actualizacion')[:5]

    datos = {
        'products5': listproducts5}

    return render(request, 'core/favoritos.html', datos)

def showDetail(request, id):
    producto = get_object_or_404(Producto, id=id)
    form = ComentarioForm()

    comentarios = Comentario.objects.filter(producto=producto).select_related('usuario')

    page = request.GET.get('page', 1)
    paginator = Paginator(comentarios, 5)  
    try:
        comentarios_paginated = paginator.page(page)
    except PageNotAnInteger:
        comentarios_paginated = paginator.page(1)
    except EmptyPage:
        comentarios_paginated = paginator.page(paginator.num_pages) 

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user  
            comentario.producto = producto 
            comentario.save()
            messages.success(request, 'Comentario agregado correctamente.')
            return render(request, 'core/detail.html', {
                'producto': producto,
                'form': form,
                'comentarios': comentarios_paginated,
                'paginator': paginator,
            })
        else:
            messages.error(request, 'El comentario no ha sido agregado. Por favor, revisa la información.')

    return render(request, 'core/detail.html', {
        'producto': producto,
        'form': form,
        'comentarios': comentarios_paginated,
        'paginator': paginator,
    })

def showAboutUs(request):
    return render(request, 'core/aboutus.html')

def showContact(request):
    return render(request, 'core/contactos.html')

def showAdmin(request):
    return render(request, 'core/admin.html')

@permission_required('app.add_product')
def addProduct(request):

    datos = {'form': ProductoForm()}

    if request.method == 'POST':
        form = ProductoForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            datos['msj'] = 'Producto agregado correctamente'
        else:
            datos['msj'] = 'El producto no ha sido agregado'

    return render(request, 'core/Products/add.html', datos)

@permission_required('app.view_product')
def listProduct(request):

    listproduct = Producto.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(listproduct, 5)
        listproduct = paginator.page(page)
    except:
        raise Http404

    datos = {'entity': listproduct,
            'paginator': paginator}

    return render(request, 'core/Products/list.html', datos)

@permission_required('app.change_product')
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

    return render(request, 'core/Products/update.html', datos)

@permission_required('delete.add_product')
def deleteProduct(request, id):

    user = Producto.objects.get(id=id)
    user.delete()

    return redirect(to="list")





