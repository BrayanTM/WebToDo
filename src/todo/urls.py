from django.urls import path
from .views import ListarTareas, DetalleTarea, CrearTarea, ActualizarTarea, EliminarTarea, CustomLoginView, RegistroUsuario
from django.contrib.auth.views import LogoutView

urlpatterns = [path('login/', CustomLoginView.as_view(), name='login'),
               path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
                path('registro/', RegistroUsuario.as_view(), name='registro'),
               path('', ListarTareas.as_view(), name='lista_pendientes'),
               path('detalle/<int:pk>', DetalleTarea.as_view(), name='detalle_tarea'),
               path('crear-tarea/', CrearTarea.as_view(), name='crear_tarea'),
               path('editar-tarea/<int:pk>', ActualizarTarea.as_view(), name='actualizar_tarea'),
               path('eliminar-tarea/<int:pk>', EliminarTarea.as_view(), name='eliminar_tarea')]