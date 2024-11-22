from django.urls import path
from .views import *

urlpatterns = [
    path('', showIndex, name='index'),
    path('index/', showIndex, name='index'),
    path('registro/', showRegistro, name='registro'),
    path('search/', showSearch, name='search'),
    path('detail/<int:id>/', showDetail, name='detail'),
    path('contact/', showContact, name='contact'),
    path('aboutus/', showAboutUs, name='aboutus'),
    path('admin/', showAdmin, name='admin'),
    path('add/', addCar, name='add'),
    path('list/', listCar, name='list'),
    path('update/<id>/', updateCar, name='update'),
    path('delete/<id>/', deleteCar, name='delete'),
    path('favoritos/', showFavorite, name='favoritos'),
]
