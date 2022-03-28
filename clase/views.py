import re
from django.shortcuts import render
from clase.models import Curso
import random
from django.http import HttpResponse

# Create your views here.


def nuevo_curso(request):
    camada = random.randrange(1500, 3000)
    nuevo_curso = Curso(nombre='Curso Python', camada=camada)
    nuevo_curso.save()
    return HttpResponse(f"Se creo el curso {nuevo_curso.nombre} camada {nuevo_curso.camada}")

def formulario_curso(request):
    
    print(request.method)
    if request.method == 'POST':
        print(request.POST)
        nuevo_curso = Curso(nombre=request.POST['curso'], camada=request.POST['camada'])
        nuevo_curso.save()
        return render(request, 'clase/formulario_curso.html',{'nuevo_curso':nuevo_curso})
    
    return render(request, 'clase/formulario_curso.html',{})