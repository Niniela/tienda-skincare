from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    unidad_medida = models.CharField(max_length=50)  
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    foto = models.ImageField(upload_to='productos/')

    def __str__(self):
        return self.nombre
    