from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User 
from django.core.exceptions import ValidationError  
from AppDirectorio.models import *

class UsuarioRegistroForm(UserCreationForm):
    username = forms.CharField(max_length=20, label='Usuario',widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=150, label="Nombre",widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=150, label="Apellido",widget=forms.TextInput(attrs={'class': 'form-control'}))    
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2= forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}

class UsuarioEdicionForm(UserChangeForm):
    password = None
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=20, label='Nombre',widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=20, label='Apellido',widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

class CambioPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label=("Password Actual"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label=("Nuevo Password"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label=("Repita Nuevo Password"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

class NegocioCreacionFormulario(forms.Form):
    tipo_negocio = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class': 'form-control'}))
    nombre_negocio = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcion = forms.TextInput()
    direccion = forms.CharField(max_length=250,widget=forms.TextInput(attrs={'class': 'form-control'}))
    horario = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono_contacto = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email_contacto = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha_publicacion = forms.DateField()
    imagen_negocio = forms.ImageField()

    class Meta:
        model = Negocio
        fields = ['usuario', 'tipo_negocio', 'nombre_negocio', 'descripcion', 'direccion', 'horario','telefono_contacto', 'email_contacto', 'imagen_negocio']
            #saca los mensajes de ayuda
        help_texts = {k: "" for k in fields}


class ComentarioFormulario(forms.Form):
    titulo = forms.CharField(max_length=100)
    descripcion = forms.TextInput()
    fechaCalificacion = forms.DateTimeField(label="Fecha Comentario")

    class Meta:
        model = Comentario
        fields = ['titulo','descripcion','fechaCalificacion']
