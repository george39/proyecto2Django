from django.shortcuts import render
from django.views.generic import ListView
from .models import Autor

# managers
from .manager import AutorManager

# Create your views here.
class ListAutores(ListView):
   
    context_object_name = 'lista_autores'
    template_name = 'autores/lista.html'


    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        


        return Autor.objects.buscar_autor5(palabra_clave)
