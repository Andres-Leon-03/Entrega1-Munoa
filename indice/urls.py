from .views import inicio,otra_vista,numero_random,numero_del_usuario,mi_plantilla
from django.urls import path
   
urlpatterns=[
    path('inicio/', inicio),
    path('numero-random/', numero_random),
    path('dame-numero/<numero>', numero_del_usuario),
    # path('dame-numero/<int:numero>', numero_del_usuario), CON EL INT ASEGURAMOS QUE ES ENTERO
    path('mi-plantilla', mi_plantilla),
    path('', otra_vista),
    
] 
    