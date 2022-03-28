from django.shortcuts import render

# Create your views here.

from contextvars import Context
from urllib.error import ContentTooShortError
from multiprocessing import context
from pipes import Template
from django.http import HttpResponse
import random

from django.template import Context,Template,loader

def inicio(request):
    return HttpResponse('HOLA MUNDO')


def otra_vista(request):
    return HttpResponse('''
                        <h1>Otra Vista</h1>
                        ''')
    
    
def numero_random(request):
    numero = random.randrange(15,180)
    texto = f'<h1>Este es un numero random: {numero}</h1>'
    # return HttpResponse(numero)
    return HttpResponse(texto)
    
    
def numero_del_usuario(request,numero):
    texto = f'<h1>Este es un numero random: {numero}</h1>'
    # return HttpResponse(numero)
    return HttpResponse(texto)


def mi_plantilla(request):
    # plantilla = open(r"C:\Users\andre\Desktop\miproyecto\miproyecto\plantillas\mi_plantilla.html")
    # template = Template(plantilla.read())
    # plantilla.close()
    
    template=loader.get_template("mi_plantilla.html")
    
     
    nombre="Andres"
    apellido="Muñoa"
    lista=[5,6,4,7,5525,4]
    
    diccionario_de_datos={
        'nombre': nombre,
        'apellido': apellido,
        'nombre_largo':len(nombre),
        'lista':lista
    }
    
    # context = Context(diccionario_de_datos)
    # plantilla_preparada = template.render(context) ESTO ES PARA EL "OPEN"
    plantilla_preparada = template.render(diccionario_de_datos)
    
    return HttpResponse(plantilla_preparada)