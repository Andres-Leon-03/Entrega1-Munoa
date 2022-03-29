from django.contrib import admin
from .models import Curso, Profesor, Entregable, Estudiante, Farmacias, Medicamentos, Hospitales

# Register your models here.
admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Entregable)
admin.site.register(Estudiante)
admin.site.register(Farmacias)
admin.site.register(Medicamentos)
admin.site.register(Hospitales)