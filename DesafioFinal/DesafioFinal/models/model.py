from django.db import models

# Create your models here.
class Televisores(models.Model):
    
    nombre = models.CharField(max_length=40)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to = 'images/')
    date_update = models.DateTimeField( auto_now_add=True)


    class Meta:
        verbose_name = 'Televisores'

    def __str__(self):
        return self.nombre

class Celulares(models.Model):
    
    nombre = models.CharField(max_length=40)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to = 'images/')
    date_update = models.DateTimeField( auto_now_add=True)


    class Meta:
        verbose_name = 'Celulares'

    def __str__(self):
        return self.nombre     

class Notebooks(models.Model):
    
    nombre = models.CharField(max_length=40)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to = 'images/')
    date_update = models.DateTimeField( auto_now_add=True)


    class Meta:
        verbose_name = 'Notebooks'

    def __str__(self):
        return self.nombre 