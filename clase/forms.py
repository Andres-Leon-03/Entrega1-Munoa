from django import forms

class Farmacias(forms.Form):
    nombre = forms.CharField(max_length=20)
    direccion = forms.CharField(max_length=20)
    

class Medicamentos(forms.Form):
    nombre = forms.CharField(max_length=20)

    


class Hospitales(forms.Form):
    nombre = forms.CharField(max_length=20)
    direccion = forms.CharField(max_length=20)



class BusquedaMedicamentos(forms.Form):
    partial_medicamento = forms.CharField(max_length=20, label='Buscador')   
    
    

class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=20)
    camada = forms.IntegerField()
    
   
   

class BusquedaCurso(forms.Form):
    partial_curso = forms.CharField(max_length=20, label='Buscador')