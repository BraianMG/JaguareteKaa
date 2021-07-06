from django.urls import path, include
from . import views

urlpatterns = [
    path('acerca-de/', views.acerca_de, name="acerca_de"),
    path('contacto/', views.contacto, name="contacto"),
    path('registro/', views.pagina_registro, name="pagina_registro"),
    path('login/', views.pagina_login, name="pagina_login"),
    path('logout/', views.cerrar_sesion, name="cerrar_sesion"),
    path('', include('ecommerce.urls')),
]
