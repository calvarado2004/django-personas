from django.shortcuts import render
from django.http import HttpResponse
from personas.models import Persona, Domicilio
# Create your views here.

def bienvenido(request):
    no_personas = Persona.objects.count()
    personas = Persona.objects.order_by('id','nombre')
    dic_no_personas = {'no_personas': no_personas,
                       'personas': personas
                       }
    return render(request, 'bienvenido.html', dic_no_personas)

def despedirse(request):
    return HttpResponse('Despedida desde Django')

def contacto(request):
    return HttpResponse('Contacto: -Teléfono: 9804473408, -email: calvarado2004@gmail.com')

def domicilios(request):
    no_domicilios = Domicilio.objects.count()
    domicilios = Domicilio.objects.order_by('id')
    dic_no_domicilios = {'no_domicilios': no_domicilios,
                         'domicilios': domicilios
                         }
    return render(request, 'domicilios.html', dic_no_domicilios)