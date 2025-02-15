"""Verificacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Verificacion.views import saludos, fecha, calculoedad
from . import views
#ACA VAN LAS URLS, Cuando se llama a una funcion que esta en otro archivo hay que importarla
urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludos', saludos),
    path('fecha/', fecha),
    #lo que tiene int convierte las ultimas 2 cosas de la url en numeros y lo guarda como parametro para el view
    path('calculoedad/<int:edad>/<int:agno>', calculoedad),
]