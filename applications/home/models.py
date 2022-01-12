from django.db import models

# Create your models here.
class Persona(models.Model):

    full_name = models.CharField('nombres', max_length=50)
    pais = models.CharField('Pais', max_length=50)
    pasaporte = models.CharField('Pasaporte', max_length=50)
    edad = models.IntegerField()
    apelativo = models.CharField('Apelativio', max_length=10)


    class Meta:

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        db_table = 'persona'  # nombre con el cual se va a crear la tabla en la bd
        unique_together = ['pais', 'apelativo'] #para que no se registre un pais con el mismo nombre de apelativo
    # para que registre edad >= a 18
        constraints = [
            models.CheckConstraint(check=models.Q(edad__gte=18), name='edad_mayor_18')
        ]
       # abstract = True  # para que el modelo no se cree en la base de datos

    def __str__(self):
        return self.full_name   



# HERENCIA
class  Empleado(Persona):
    empleo = models.CharField('empleo', max_length=50)      
