from django.db import models

class Carro(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    velocidad_maxima = models.IntegerField()
