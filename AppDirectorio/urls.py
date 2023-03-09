from django.urls import path
from AppDirectorio import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.inicio, name="Inicio"),
    path('registroUsuarios', views.registro_usuarios, name="Registro"),
    path('login', views.inicio_sesion, name="Login")
]