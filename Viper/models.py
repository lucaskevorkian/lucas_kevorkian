from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Auto(models.Model):
    marca = models.CharField(max_length=100, default="Dodge")
    modelo = models.CharField(max_length=100, null=False)
    año = models.IntegerField(default=2024, validators=[MinValueValidator(0)], error_messages={'invalid': 'El año no puede ser negativo.'})
    precio = models.IntegerField(default=0, validators=[MinValueValidator(0)], error_messages={'invalid': 'El año no puede ser negativo.'})
    hp = models.IntegerField(default=0, validators=[MinValueValidator(0)], error_messages={'invalid': 'El año no puede ser negativo.'})
    foto = models.ImageField(upload_to="autos", blank=True, null=True)
    foto_url = models.URLField(blank=True, null=True)
    
    def __str__(self):  #mostrar en admin o al cliente los nombres de los modelos
        return f"{self.id}° {self.marca} {self.modelo}, {self.año}"


class Avion(models.Model):
    modelo = models.CharField(max_length=100, null=False)
    año = models.IntegerField()
    altitud = models.IntegerField()
    foto = models.ImageField(upload_to="aviones", blank=True, null=True)
    
    
    def __str__(self):
        return f"{self.id}° {self.modelo} {self.año} {self.altitud}mts"