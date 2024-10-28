from django.urls import path
from .views import *

urlpatterns = [
    path('', mostrarindex, name='index'),
    path('login/', mostrarlogin, name='login'),
    path('registro/', mostrarregistro, name='registro'),
    path('index/', mostrarindex, name='index'),
    path('contactos/', mostrarcontactos, name='contactos'),
    path('search/', mostrarsearch, name='search'),
    path('favoritos/', mostrarfavoritos, name='favoritos'),
    path('aboutus/', mostraraboutus, name='aboutus'),
    path('admin/', mostraradmin, name='admin'),
    path('add/', adduser, name='add'),
    path('list/', listuser, name='list'),
    path('update/<id>/', updateuser, name='update'),
    path('delete/<id>/', deleteuser, name='delete')
]
