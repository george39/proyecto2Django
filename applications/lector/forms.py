from django import forms
from django.forms import widgets
from applications.libro.models import Libro
from .models import Prestamo


class PrestamoForm(forms.ModelForm):

    class Meta:
        model = Prestamo
        fields = (
            'lector',
            'libro'
        )


class MultiplePrestamoForm(forms.ModelForm):
    libros = forms.ModelMultipleChoiceField(
        queryset=None,
        required=True,
        widget=forms.widgets.CheckboxSelectMultiple,
    )   

    class Meta:
        model = Prestamo
        fields = (
            'lector',
        )  

# inicializar valores
    def __init__(self, *args, **kwargs):
        super(MultiplePrestamoForm, self).__init__(*args, **kwargs)
        self.fields['libros'].queryset = Libro.objects.all()