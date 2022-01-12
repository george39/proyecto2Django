from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('libros-2/', views.ListarLibros2.as_view(), name='libros2'),
    path('detail-libro/<pk>/', views.LibroDetailView.as_view(), name='detalle')
]