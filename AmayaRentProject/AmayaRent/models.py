from django.db import models

# Create your models here.
class AptoTemporales(models.Model):
    direccion = models.CharField(max_length=300)
    precio = models.IntegerField()
    disponibilidad = models.BooleanField()
    
class Contactos(models.Model):
    nombre = models.CharField(max_length=40)
    contacto = models.IntegerField()
    
    