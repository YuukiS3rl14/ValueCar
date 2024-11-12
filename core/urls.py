from django.urls import path
from .views import *

urlpatterns = [
    path('', showIndex, name='index'),
    path('login/', showLogin, name='login'),
    path('registro/', showRegister, name='registro'),
    path('index/', showIndex, name='index'),
    path('contactos/', showContact, name='contactos'),
    path('search/', showSearch, name='search'),
    path('favoritos/', showFavorite, name='favoritos'),
    path('aboutus/', showAboutUs, name='aboutus'),
    path('admin/', showAdmin, name='admin'),
    path('add/', addProduct, name='add'),
    path('list/', listProduct, name='list'),
    path('update/<id>/', updateProduct, name='update'),
    path('delete/<id>/', deleteProduct, name='delete')
]
