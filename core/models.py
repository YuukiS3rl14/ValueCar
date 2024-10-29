from django.db import models

# Create your models here.

class Region(models.Model):
    numero = models.IntegerField()
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Supermercado(models.Model):
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    supermercado = models.ForeignKey(Supermercado, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    precio = models.IntegerField() 
    descripcion = models.CharField(max_length=300)
    imagen_url = models.ImageField()
    origen_url = models.CharField(max_length=300)
    fecha_actualizacion = models.DateField()

    def __str__(self):
        return self.nombre 
    
class Rol(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre 
    
class Usuario(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=300)
    contraseña = models.CharField(max_length=256)

    def __str__(self):
        return self.nombre 

class Comentario(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.CharField(max_length=50)
    calificacion = models.IntegerField() 
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo



