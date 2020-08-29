"""sap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import include, url

from personas.views import detallePersona, nuevaPersona, editarPersona, eliminarPersona, nuevoDomicilio, editarDomicilio, eliminarDomicilio, detalleDomicilio
from webapp.views import bienvenido, despedirse, contacto, domicilios



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenido, name='index'),
    path('despedida/', despedirse),
    path('contacto/', contacto),
    path('detalle_persona/<int:id>', detallePersona),
    path('nueva_persona/', nuevaPersona),
    path('editar_persona/<int:id>',editarPersona),
    path('eliminar_persona/<int:id>',eliminarPersona),
    path('domicilios/detalle_domicilio/<int:id>',detalleDomicilio),
    path('domicilios/nuevo_domicilio/',nuevoDomicilio),
    path('domicilios/editar_domicilio/<int:id>',editarDomicilio),
    path('domicilios/eliminar_domicilio/<int:id>',eliminarDomicilio),
    path('domicilios/', domicilios, name='domicilios'),
]
