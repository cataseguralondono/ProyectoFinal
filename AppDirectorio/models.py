from django.db import models
from django.contrib.auth.models import User

class Negocio(models.Model):
    tipo_negocio_opciones = (
    ('ropa','Ropa'),
    ('detalles', 'Detalles'),
    ('salud','Salud'),
    ('automotriz','Automotriz'),
    ('comida','Comida'),
    ('belleza','Belleza'),
    ('otro', 'Otro'),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    tipo_negocio = models.CharField(max_length=15, choices=tipo_negocio_opciones, default='otro')
    nombre_negocio = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    direccion = models.CharField(max_length=250)
    horario = models.CharField(max_length=100)
    telefono_contacto = models.CharField(max_length=200)
    email_contacto = models.EmailField()
    fecha_publicacion = models.DateField()
    imagen_negocio = models.ImageField()

class Calificacion(models.Model):
    calificacion = models.ForeignKey(Negocio, related_name='calificacion', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    fechaCalificacion = models.DateTimeField(auto_now_add=True)





