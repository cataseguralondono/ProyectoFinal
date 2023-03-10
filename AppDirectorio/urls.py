from django.urls import path
from AppDirectorio import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.inicio, name="Inicio"),
    path('registroUsuarios', views.registro_usuarios, name="Registro"),
    path('login', views.inicio_sesion, name="Login"),
    path('negocioCreacion/<int:pk>', views.NegocioCreacion.as_view(), name='Agregar Negocio'),
    path('negocioDetalle/<int:pk>/', views.NegocioDetalle.as_view(), name='Detalle Negocio'),
    path('negocioEdicion/<int:pk>/', views.NegocioEdicion.as_view(), name='Editar Negocio'),
    path('negocioEliminar/<int:pk>/', views.NegocioEliminar.as_view(), name='Eliminar Negocio'),
    path('listarNegocios', views.NegocioLista.as_view(), name="Lista Negocios"),
    path('negocioDetalle/<int:pk>/comentario/', views.ComentarioNegocio.as_view(), name="Agregar Comentario"),

]