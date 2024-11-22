from django.contrib import admin
from .models import *

# Register your models here.

class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'numero', 'nombre']
    search_fields = ['id', 'numero', 'nombre']
    list_per_page = 10

class ComunaAdmin(admin.ModelAdmin):
    list_display = ['id', 'region', 'nombre']
    search_fields = ['id', 'region', 'nombre']
    list_per_page = 10

class AutomotoraAdmin(admin.ModelAdmin):
    list_display = ['id', 'comuna', 'nombre']
    search_fields = ['id', 'comuna', 'nombre']
    list_per_page = 10

class TipoCombustibleAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['id', 'nombre']
    list_per_page = 10

class TipoTransmicionAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['id', 'nombre']
    list_per_page = 10

class AutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'automotora', 'nombre', 'marca', 'modelo', 'año', 'precio','descripcion','imagen','origen','fecha_actualizacion','kilometraje','tipo_combustible','potencia','tipo_transmicion','color']
    search_fields = ['id', 'automotora', 'nombre', 'marca', 'modelo', 'año', 'precio','descripcion','imagen','origen','fecha_actualizacion','kilometraje','tipo_combustible','potencia','tipo_transmicion','color']
    list_per_page = 10

class RolAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['id', 'nombre']
    list_per_page = 10

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'texto', 'calificacion', 'usuario', 'auto']
    search_fields = ['titulo', 'texto', 'calificacion', 'usuario', 'auto']
    list_per_page = 10

class FavoritoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'auto']
    search_fields = ['usuario', 'auto']
    list_per_page = 10

admin.site.register(Region, RegionAdmin)
admin.site.register(Comuna, ComunaAdmin)
admin.site.register(Automotora, AutomotoraAdmin)
admin.site.register(TipoCombustible, TipoCombustibleAdmin)
admin.site.register(TipoTransmicion, TipoTransmicionAdmin)
admin.site.register(Auto, AutoAdmin)
admin.site.register(Rol, RolAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Favorito, FavoritoAdmin)
