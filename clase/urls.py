from django.urls import path
from .views import nuevo_curso,formulario_curso,busqueda_curso,formulario_farmacias,formulario_medicamentos, formulario_hospitales,busqueda_medicamentos



urlpatterns = [
    path('nuevo/', nuevo_curso, name="nuevo_curso"),
    path('farmacia/', formulario_farmacias, name="formulario_farmacias"),
    path('medicamento/', formulario_medicamentos, name="formulario_medicamentos"),
    path('hospitales/', formulario_hospitales, name="formulario_hospitales"),
    path('curso/', formulario_curso, name="formulario_curso"),
    path('busqueda-curso/', busqueda_curso, name="busqueda_curso"),
    path('busqueda-medicamentos/', busqueda_medicamentos, name="busqueda_medicamentos"),
    
]