from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name='id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='nombre de la categoria')

    def __str__(self):
        return self.nombreCategoria

class Cliente(models.Model):
    nombre = models.CharField(max_length=8, primary_key=True,verbose_name='nombre')
    apellido = models.CharField(max_length=12, verbose_name='apellido')
    ciudad = models.CharField(max_length=12, verbose_name='ciudad')
    edad = models.CharField(max_length=3, null=True,blank = True, verbose_name='edad')
    categoria = models.ForeignKey(Categoria,on_delete= models.CASCADE)

    def __str__(self):
        return self.nombre