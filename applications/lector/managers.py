from django.db import models 
from django.db.models import Q, Avg, Sum
from django.db.models.aggregates import Count
from django.db.models.functions import Lower



# MANAGER PARA EL MODELO LECTOR
class PrestamoManager(models.Manager):
    # Promedio de edades que prestan un libro

    def libro_promedio_edad(self):
        resultado = self.filter(
            libro__id = '8'
        ).aggregate(
            promedio_edad = Avg('lector__edad'),
            suma_edad=Sum('lector__edad')
        )
        return resultado


   # Contar cantidad de libros prestados
    def num_libros_prestados(self):
        resultado =  self.values(
            'libro'
        ).annotate(
            num_prestados = Count('libro'),
            titulo = Lower('libro__titulo')
        )  
        for r in resultado:
            print('+++++++++++++++')
            print(r, r['num_prestados'])