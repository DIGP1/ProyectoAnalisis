from django.db import models

# Create your models here.

class usuarios(models.Model):
    #id= models.IntegerField(primary_key=True)
    Nombre= models.CharField(max_length=50)
    correo= models.CharField(max_length=15)
    usuario= models.CharField(max_length=10)
    contraseña= models.CharField(max_length=15)
    def __str__(self) -> str:
        return self.Nombre
    

class datosEjercicio(models.Model):
    fx=models.DecimalField(max_digits=5, decimal_places=5)
    h0=models.DecimalField(max_digits=5, decimal_places=5)
    h1=models.DecimalField(max_digits=5, decimal_places=5)
    Sg0=models.DecimalField(max_digits=5, decimal_places=5)
    Sg1=models.DecimalField(max_digits=5, decimal_places=5)
    A=models.DecimalField(max_digits=5, decimal_places=5)
    B=models.DecimalField(max_digits=5, decimal_places=5)
    C=models.DecimalField(max_digits=5, decimal_places=5)
    x3=models.DecimalField(max_digits=5, decimal_places=5)
    Iteracion= models.IntegerField(max_length=5)
    RaizAnterior= models.DecimalField(max_digits=5, decimal_places=5)
    RaizResultante= models.DecimalField(max_digits=5, decimal_places=5)
    MargenError= models.DecimalField(max_digits=5, decimal_places=5)
    def __str__(self) -> str:
        return self.h0


