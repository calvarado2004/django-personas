from django.db import models

# Create your models here.
class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    no_calle = models.IntegerField()
    pais = models.CharField(max_length=255)

    def __str__(self):
        return f'Calle: {self.calle},  ' \
               f'Número: {self.no_calle}, ' \
               f'País: {self.pais}'

class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Persona {self.id}: {self.nombre} {self.apellido} {self.email}'
