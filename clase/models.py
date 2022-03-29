from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesión = models.CharField(max_length=30)
  
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
  
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=20)
    fechaDeEntrega = models.DateTimeField()
    entregado = models.BooleanField()
    
    
class Curso(models.Model):
    nombre = models.CharField(max_length=20)
    camada = models.IntegerField()
    
    def __str__(self):
        return f"Curso: {self.nombre} - Camada: {self.camada}"
    
   
#CLASES PARA EL ENTREGABLE
class Farmacias(models.Model):
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    
    
    
class Medicamentos(models.Model):
    nombre = models.CharField(max_length=20)
    
    def __str__(self):
        return f"Nombre del medicamento: {self.nombre}"
    
    


class Hospitales(models.Model):
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)