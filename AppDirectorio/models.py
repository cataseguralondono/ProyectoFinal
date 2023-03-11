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
    descripcion = models.TextField()
    direccion = models.CharField(max_length=250)
    horario = models.CharField(max_length=100)
    telefono_contacto = models.CharField(max_length=200)
    email_contacto = models.EmailField()
    fecha_publicacion = models.DateField(auto_now_add=True)
    imagen_negocio = models.ImageField(upload_to="imagenes/")

    def __str__(self):
        return self.nombre_negocio

class Comentario(models.Model):
    negocio = models.ForeignKey(Negocio, related_name='comentario', on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    fecha_comentario = models.DateTimeField(auto_now_add=True)




