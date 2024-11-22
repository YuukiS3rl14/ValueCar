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
    listautos5 = Auto.objects.order_by('-fecha_actualizacion')[:5]
    autoslider = Auto.objects.filter(automotora__nombre='Lider')
    autosjumbo = Auto.objects.filter(automotora__nombre='Jumbo')
    autossanta_isabel = Auto.objects.filter(automotora__nombre='Santa Isabel')
    
    lider_autos = [autoslider[i:i + 5] for i in range(0, len(autoslider), 5)]
    jumbo_autos = [autosjumbo[i:i + 5] for i in range(0, len(autosjumbo), 5)]
    santa_isabel_autos = [autossanta_isabel[i:i + 5] for i in range(0, len(autossanta_isabel), 5)]

    datos = {
        'autos5': listautos5,
        'lider_autos': lider_autos,
        'jumbo_autos': jumbo_autos,
        'santa_isabel_autos': santa_isabel_autos,
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
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
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

    results = Auto.objects.all()

    if query:
        results = results.filter(
            Q(nombre__icontains=query) | 
            Q(marca__icontains=query) | 
            Q(descripcion__icontains=query) | 
            Q(automotora__nombre__icontains=query)
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
        results = results.filter(automotora__nombre=market)
    if name_initial:
        results = results.filter(nombre__istartswith=name_initial)

    return render(request, 'core/search.html', {'results': results, 'query': query, 'mostrar_filtros': True})

@login_required
def showFavorite(request):
    listautos5 = Auto.objects.order_by('-fecha_actualizacion')[:5]

    datos = {
        'autos5': listautos5
    }

    return render(request, 'core/favoritos.html', datos)

def showDetail(request, id):
    auto = get_object_or_404(Auto, id=id)
    form = ComentarioForm()

    comentarios = Comentario.objects.filter(auto=auto).select_related('usuario')

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
            comentario.auto = auto 
            comentario.save()
            messages.success(request, 'Comentario agregado correctamente.')
            return render(request, 'core/detail.html', {
                'auto': auto,
                'form': form,
                'comentarios': comentarios_paginated,
                'paginator': paginator,
            })
        else:
            messages.error(request, 'El comentario no ha sido agregado. Por favor, revisa la información.')

    return render(request, 'core/detail.html', {
        'auto': auto,
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

@permission_required('core.add_auto')
def addCar(request):
    datos = {'form': AutoForm()}

    if request.method == 'POST':
        form = AutoForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            datos['msj'] = 'Auto agregado correctamente'
        else:
            datos['msj'] = 'El auto no ha sido agregado'

    return render(request, 'core/Car/add.html', datos)

@permission_required('core.view_auto')
def listCar(request):
    listaautos = Auto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(listaautos, 5)
        listaautos = paginator.page(page)
    except:
        raise Http404

    datos = {'entity': listaautos,
              'paginator': paginator}

    return render(request, 'core/Car/list.html', datos)

@permission_required('core.change_auto')
def updateCar(request, id):
    auto = Auto.objects.get(id=id)
    datos = {'form': AutoForm(instance=auto)}

    if request.method == 'POST':
        form = AutoForm(data=request.POST, instance=auto, files=request.FILES)
        if form.is_valid():
            form.save()
            datos['msj'] = 'Auto modificado correctamente'
            datos['form'] = form
        else:
            datos['msj'] = 'El auto no ha sido modificado'

    return render(request, 'core/Car/update.html', datos)

@permission_required('core.delete_auto')
def deleteCar(request, id):
    auto = Auto.objects.get(id=id)
    auto.delete()

    return redirect(to="list")