from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('pruebas', views.buscar),
    path('Registro',views.registrarUsuario),
    path('inicioSesion', views.inicioSesion),
    path('cerrarSesion', views.cerrarSesion)
]