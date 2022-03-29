import re
from django.shortcuts import render
from clase.models import Curso,Farmacias,Medicamentos,Hospitales
import random
from django.http import HttpResponse
from clase.forms import CursoFormulario, BusquedaCurso, FarmaciasFormulario, MedicamentosFormulario, HospitalesFormulario, BusquedaMedicamentos

# Create your views here.


def nuevo_curso(request):
    camada = random.randrange(1500, 3000)
    nuevo_curso = Curso(nombre='Curso Python', camada=camada)
    nuevo_curso.save()
    return HttpResponse(f"Se creo el curso {nuevo_curso.nombre} camada {nuevo_curso.camada}")

def formulario_curso(request):
    
    # SIN FORMULARIOS DE DJANGO
    # print(request.method)
    # if request.method == 'POST':
    #     print(request.POST)
    #     nuevo_curso = Curso(nombre=request.POST['curso'], camada=request.POST['camada'])
    #     nuevo_curso.save()
    #     return render(request, 'indice/index.html',{'nuevo_curso':nuevo_curso})
    
    # return render(request, 'clase/formulario_curso.html',{})
    
    
    #CON FORMUALRIO DE DJANGO
    if request.method == 'POST':
        formulario = CursoFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_curso = Curso(nombre=data['curso'], camada=data['camada'])
            nuevo_curso.save()
            return render(request, 'indice/index.html',{'nuevo_curso':nuevo_curso})
            
        
    formulario = CursoFormulario()   
    return render(request, 'clase/formulario_curso.html',{'formulario':formulario})




def busqueda_curso(request):
    cursos_buscados = []
    dato = request.GET.get('partial_curso', None)
    
    if dato is not None:
        #cursos_buscados = Curso.objects.filter(nombre=dato)
        #cursos_buscados = Curso.objects.get(nombre=dato)
        cursos_buscados = Curso.objects.filter(nombre__icontains=dato)
    
    buscador = BusquedaCurso()
    return render(
            request, "clase/busqueda_curso.html",
            {'buscador':buscador,'cursos_buscados':cursos_buscados, 'dato':dato}
            )
    
    
    
# FORMULARIOS PARA EL ENTREGABLE
def formulario_curso(request):
    if request.method == 'POST':
        formulario = CursoFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_curso = Curso(nombre=data['curso'], camada=data['camada'])
            nuevo_curso.save()
            return render(request, 'indice/index.html',{'nuevo_curso':nuevo_curso})
            
        
    formulario = CursoFormulario()   
    return render(request, 'clase/formulario_curso.html',{'formulario':formulario})




def formulario_farmacias(request):
    if request.method == 'POST':
        formulario = FarmaciasFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            formulario_farmacias = Farmacias(nombre=data['nombre'], direccion=data['direccion'])
            formulario_farmacias.save()
            return render(request, 'indice/index.html',{'formulario_farmacias':formulario_farmacias})
            
        
    formulario = FarmaciasFormulario()   
    return render(request, 'clase/formulario_farmacias.html',{'formulario':formulario})



def formulario_medicamentos(request):
    if request.method == 'POST':
        formulario = MedicamentosFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            formulario_medicamentos = Medicamentos(nombre=data['nombre'])
            formulario_medicamentos.save()
            return render(request, 'indice/index.html',{'formulario_medicamentos':formulario_medicamentos})
            
        
    formulario = MedicamentosFormulario()   
    return render(request, 'clase/formulario_medicamentos.html',{'formulario':formulario})


def formulario_hospitales(request):
    if request.method == 'POST':
        formulario = HospitalesFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            formulario_hospitales = Hospitales(nombre=data['nombre'], direccion=data['direccion'])
            formulario_hospitales.save()
            return render(request, 'indice/index.html',{'formulario_hospitales':formulario_hospitales})
            
        
    formulario = HospitalesFormulario()   
    return render(request, 'clase/formulario_hospitales.html',{'formulario':formulario})




def busqueda_medicamentos(request):
    medicamentos_buscados = []
    dato = request.GET.get('partial_medicamento', None)
    
    if dato is not None:
        medicamentos_buscados = Medicamentos.objects.filter(nombre__icontains=dato)
    
    buscador = BusquedaMedicamentos()
    return render(
            request, "clase/busqueda_medicamentos.html",
            {'buscador':buscador,'medicamentos_buscados':medicamentos_buscados, 'dato':dato}
    )