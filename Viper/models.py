from django.db import models

class Auto(models.Model):
    marca = models.CharField(max_length=100, default="Dodge")
    modelo = models.CharField(max_length=100, null=False)
    año = models.IntegerField(default=2024)
    
    def __str__(self):  #mostrar en admin o al cliente los nombres de los modelos
        return f"{self.id}° {self.marca} {self.modelo}, {self.año}"
