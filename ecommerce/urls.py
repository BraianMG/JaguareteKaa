from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('inicio/', views.index, name="inicio"), # URL alternativa para ir al Inicio
    path('busqueda/<int:id_categoria>', views.busqueda, name="busqueda"),
    path('busqueda/<str:palabra>', views.busqueda, name="busqueda"),
    path('nuevo-producto/', views.nuevo_producto, name="nuevo_producto"),
    path('producto/<int:id_producto>', views.detalle_producto, name="detalle_producto"),
    path('editar-producto/<int:id_producto>', views.editar_producto, name="editar_producto"),
    path('eliminar-producto/<int:id_producto>', views.eliminar_producto, name="eliminar_producto"),
]

