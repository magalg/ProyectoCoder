from django.db import models


class Familia(models.Model):
    nombre = models.CharField(max_length=30)
    anio = models.IntegerField()
    fecha_nac = models.DateField()