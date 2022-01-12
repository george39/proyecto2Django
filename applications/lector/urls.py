from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('prestamo/', views.AddPrestamo.as_view(), name='prestamo'),
    path('multiple-prestamo/', views.AddMultiplePrestamo.as_view(), name='add_multiple_prestamo')
]