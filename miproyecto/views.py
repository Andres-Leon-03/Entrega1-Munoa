from contextvars import Context
from urllib.error import ContentTooShortError
from multiprocessing import context
from pipes import Template
from django.http import HttpResponse
import random

from django.template import Context,Template

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
    plantilla = open(r"C:\Users\andre\Desktop\miproyecto\miproyecto\plantillas\mi_plantilla.html")
    template = Template(plantilla.read())
    context = Context()
    plantilla_preparada = template.render(context)
    return HttpResponse(plantilla_preparada)