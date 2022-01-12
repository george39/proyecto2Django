import datetime
from django.db import models 
from django.db.models import Q, Count
from django.db.models.expressions import OrderBy

#from .models import Categoria



# MANAGER PARA EL MODELO AUTOR
class LibroManager(models.Manager):
    def listar_libros1(self, kword):
        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range = ('2022-01-06', '2022-01-09')
        )
        return resultado    


    def listar_libros2(self, kword, fecha1, fecha2):

        # Para navegadores que no combierten la fecha
        date1 = datetime.datetime.strptime(fecha1, '%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(fecha2, '%Y-%m-%d').date()

        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range = (date1, date2)
        )
        return resultado 


    # LISTAR LIBROS POR CATEGORIA
    def listar_libros_categoria(self, categoria):

        return self.filter(
            categoria__id=categoria
        ).order_by('titulo')    
    

    # AGREGAR UN AUTOR
    def add_autor_libro(self, libro_id, autor):
        libro = self.get(id=libro_id)
        libro.autores.add(autor)
        return libro


    # ELIMINAR UN AUTOR
    def delete_autor_libro(self, libro_id, autor):
        libro = self.get(id=libro_id)
        libro.autores.remove(autor)
        return libro 


    # Cantidad de libros prestados
    def libros_num_prestamo(self):
        resultado = self.aggregate(
            num_prestamos = Count('libro_prestamo')
        )       
        return resultado

    # Contar cuantos libros estan prestados
    # def num_libros_prestados(self):
    #     resultado =  self.annotate(
    #         num_prestados = Count('libro_prestamo')
    #     )  
    #     for r in resultado:
    #         print('+++++++++++++++')
    #         print(r, r.num_prestados)    


# Manager para el modelo categoria
class CategoriaManager(models.Manager):


    def categoria_por_autor(self, autor):
        return self.filter(
            categoria_libro__autores__id=autor
        ).distinct()


    # Contar cuantos libros estan prestados
    def listar_categoria_libros(self):
        resultado = self.annotate(
            num_libros = Count('categoria_libro')
        )  
        return resultado  