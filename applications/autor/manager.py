from django.db import models 
from django.db.models import Q



# MANAGER PARA EL MODELO AUTOR
class AutorManager(models.Manager):
    def buscar_autor(self, kword):
        resultado = self.filter(
            nombre__icontains=kword
        )
        return resultado    

    def buscar_autor2(self, kword):
        resultado = self.filter(
            Q(nombre__icontains=kword) | Q(apellidos__icontains=kword)
        )
        return resultado




    def buscar_autor3(self, kword):
        resultado = self.filter(
            nombre__icontains=kword
        ).exclude(edad = 40)
        return resultado 


    def buscar_autor4(self, kword):
        resultado = self.filter(
            nombre__icontains=kword
        ).exclude(
            Q(edad__icontains=35) | Q(edad__icontains=45)
        )
        return resultado 


    def buscar_autor5(self, kword):
        resultado = self.filter(
            edad__gt=30,
            edad__lt=40
        ).order_by('apellidos', 'nombre')
        return resultado        