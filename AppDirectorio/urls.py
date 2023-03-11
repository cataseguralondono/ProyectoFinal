from django.urls import path
from AppDirectorio import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.inicio, name="Inicio"),
    path('registroUsuarios', views.registro_usuarios, name="Registro"),
    path('editarUsuarios', views.UsuarioEdicion.as_view(), name="Editar Usuario"),
    path('login', views.inicio_sesion, name="Login"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='Logout'),
    path('crearNegocio/<int:pk>', views.NegocioCreacion.as_view(), name='Agregar Negocio'),
    path('detalleNegocio/<int:pk>/', views.NegocioDetalle.as_view(), name='Detalle Negocio'),
    path('editarNegocio/<int:pk>/', views.NegocioEdicion.as_view(), name='Editar Negocio'),
    path('eliminarNegocio/<int:pk>/', views.NegocioEliminar.as_view(), name='Eliminar Negocio'),
    path('listarNegocios', views.NegocioLista.as_view(), name="Lista Negocios"),
    path('detalleNegocio/<int:pk>/comentario/', views.ComentarioNegocio.as_view(), name="Agregar Comentario"),

]