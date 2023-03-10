from django.contrib.auth import forms  
from django.shortcuts import redirect, render  
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

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
    
    return render(request, "crear_usuarios.html", {"form":form})

def inicio_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
            
            user = authenticate(username = usuario, password = clave)
            
            if user is not None:
                login(request, user)
                return render(request, "inicio.html", {"Mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "login.html", {'form':form, "Mensaje":"Error, datos incorrectos"})
        
        else:
            return render(request, "login.html", {'form':form, "Mensaje":"Error, formulario erroneo"})
    
    form = AuthenticationForm()
    return render(request, "login.html", {'form':form})

class NegocioCreacion(CreateView):
    model = Negocio
    success_url = reverse_lazy("Inicio")
    template_name = "crear_negocio.html"
    fields = ['tipo_negocio', 'nombre_negocio', 'descripcion', 'direccion', 'horario','telefono_contacto', 'email_contacto', 'fecha_publicacion', 'imagen_negocio']

    def form_valid(self, form, **kwargs):
        form.instance.usuario_id = self.kwargs.get('pk')
        return super(NegocioCreacion, self).form_valid(form)

class NegocioDetalle(DetailView):
    model = Negocio
    context_object_name = 'negocio'
    template_name = 'detalle_negocio.html'

class NegocioEdicion(UpdateView):
    model = Negocio
    success_url = reverse_lazy('Inicio')
    template_name = 'editar_negocio.html'
    fields = ['tipo_negocio', 'nombre_negocio', 'descripcion', 'direccion', 'horario','telefono_contacto', 'email_contacto', 'fecha_publicacion', 'imagen_negocio']

class NegocioEliminar(DeleteView):
    model = Negocio
    success_url = reverse_lazy('Lista Negocios')
    context_object_name = 'negocio'
    template_name = 'eliminar_negocio.html'

class NegocioLista(ListView):
    context_object_name = 'negocios'
    queryset = Negocio.objects.all()
    template_name = 'listar_negocios.html'

class ComentarioNegocio(CreateView):
    model = Comentario
    template_name = 'comentario.html'
    success_url = reverse_lazy('Inicio')
    fields = ['titulo','descripcion']

    def form_valid(self, form, **kwargs):
        form.instance.negocio_id = self.kwargs.get('pk')
        return super(ComentarioNegocio, self).form_valid(form)

