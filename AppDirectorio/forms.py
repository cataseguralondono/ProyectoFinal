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