from django.contrib.auth import forms  
from django.shortcuts import redirect, render  
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from AppDirectorio.forms import *  
# Create your views here.  
  
def inicio(request):
    return render(request, 'inicio.html')

"""
def registro(request):
    if request.POST == 'POST':
        form = UsuarioForm(request.POST) 
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()  
            return render(request, "inicio.html", {"mensaje": "Usuario Creado: "})

    else:  
        form = UsuarioForm()

    return render(request, 'registroUsuarios.html', {"form":form}) 
"""

def registro_usuarios(request):
    if request.method == 'POST':
        form = UsuarioRegistroForm(request.POST)
                
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "inicio.html", {"mensaje": "Usuario Creado: "})
    
    else:
        form = UsuarioRegistroForm()
    
    return render(request, "registroUsuarios.html", {"form":form})

def inicio_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            
            user = authenticate(username = usuario, password = contra)
            
            if user is not None:
                login(request, user)
                return render(request, "inicio.html", {"Mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "login.html", {'form':form, "Mensaje":"Error, datos incorrectos"})
        
        else:
            return render(request, "login.html", {'form':form, "Mensaje":"Error, formulario erroneo"})
    
    form = AuthenticationForm()
    return render(request, "login.html", {'form':form})




