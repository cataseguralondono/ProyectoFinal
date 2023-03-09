from django.urls import path
from AppDirectorio import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.inicio, name="Inicio"),
    path('registroUsuarios', views.registro_usuarios, name="Registro"),
    path('login', views.inicio_sesion, name="Login"),
    path('negocioCreacion/', views.NegocioCreacion.as_view(), name='Nuevo Negocio'),
    path('negocioEdicion/<int:pk>/', views.NegocioEdicion.as_view(), name='Edicion Negocio'),
    path('listarNegocios', views.NegocioLista.as_view(), name="Lista Negocios")

]