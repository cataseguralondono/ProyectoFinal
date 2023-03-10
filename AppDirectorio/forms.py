from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User 
from django.core.exceptions import ValidationError  
from AppDirectorio.models import *

"""class UsuarioRegistroFormulario(UserCreationForm):
    username = forms.CharField(max_length=20, label='Usuario',widget=forms.TextInput())
    #first_name = forms.CharField(max_length=150, label="Nombre",widget=forms.TextInput())
    #last_name = forms.CharField(max_length=150, label="Apellido",widget=forms.TextInput())    
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username','email','password1', 'password2')"""

class UsuarioRegistroForm(UserCreationForm):
    username = forms.CharField(max_length=20, label='Usuario',widget=forms.TextInput())
    first_name = forms.CharField(max_length=150, label="Nombre",widget=forms.TextInput())
    last_name = forms.CharField(max_length=150, label="Apellido",widget=forms.TextInput())    
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email', 'password1', 'password2']
            #saca los mensajes de ayuda
        help_texts = {k: "" for k in fields}

class NegocioCreacionFormulario(forms.Form):
    tipo_negocio = forms.CharField(max_length=15)
    nombre_negocio = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=500)
    direccion = forms.CharField(max_length=250)
    horario = forms.CharField(max_length=100)
    telefono_contacto = forms.CharField(max_length=200)
    email_contacto = forms.EmailField()
    fecha_publicacion = forms.DateField()
    imagen_negocio = forms.ImageField()

    class Meta:
        model = Negocio
        fields = ['usuario', 'tipo_negocio', 'nombre_negocio', 'descripcion', 'direccion', 'horario','telefono_contacto', 'email_contacto', 'fecha_publicacion', 'imagen_negocio']
            #saca los mensajes de ayuda
        help_texts = {k: "" for k in fields}


class ComentarioFormulario(forms.Form):
    titulo = forms.CharField(max_length=100)
    descripcion = forms.TextInput()
    fechaCalificacion = forms.DateTimeField(label="Fecha Comentario")

    class Meta:
        model = Comentario
        fields = ['titulo','descripcion','fechaCalificacion']
