from django.contrib import admin

# Register your models here.
from .models import Libro
from .models import Categoria


admin.site.register(Libro)
admin.site.register(Categoria)