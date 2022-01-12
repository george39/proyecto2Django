from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Libro

# Create your views here.
class ListaLibros(ListView):
    context_object_name = 'libros'
    template_name = 'libro/lista_libro.html'


    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')

        fecha_inicio = self.request.GET.get('fecha1', '')
        fecha_fin = self.request.GET.get('fecha2', '')

        if fecha_inicio and fecha_fin:
             return Libro.objects.listar_libros2(palabra_clave, fecha_inicio, fecha_fin)
        else:
             return Libro.objects.listar_libros1(palabra_clave)


class ListarLibros2(ListView):
    context_object_name = 'listar_libros2'
    template_name = 'libro/lista_libro2.html'

    def get_queryset(self):
        return Libro.objects.listar_libros_categoria('4')



class LibroDetailView(DetailView):
    model = Libro
    template_name = 'libro/detalle.html'