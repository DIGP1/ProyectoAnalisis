<<<<<<< HEAD
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('pruebas', views.buscar),
    path('Registro',views.registrarUsuario),
    path('inicioSesion', views.inicioSesion),
    path('cerrarSesion', views.cerrarSesion),
    path('recuperar', views.recuperar),
    path('cambiar', views.cambiar),
    path('cambiarcontra', views.cambiarcontra)
    
=======
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('pruebas', views.buscar),
    path('Registro',views.registrarUsuario),
    path('inicioSesion', views.inicioSesion),
    path('cerrarSesion', views.cerrarSesion)
>>>>>>> adea497916b6fbb42bf4fdedd9214626e0f16cf5
]