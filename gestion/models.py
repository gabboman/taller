from django.db import models

# Create your models here.


class Coche(models.Model):#Todo gira entorno al coche
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=200)
    matricula = models.CharField(max_length=25)
    fecha_entrada= models.DateTimeField('fecha_entrada')
    fecha_salida= models.DateTimeField('fecha_salida')
    averia_reparada = models.CharField(max_length=1000)

class Trabajador(models.Model):
    nombre = models.CharField(max_length=50)
    sueldo_hora= models.FloatField()


class Trabajo(models.Model):#Un trabajo queda identificado por un coche y un trabajador. Pueden haber varios. Posible mejora de relacion.
    coche = models.ForeignKey(Coche)
    trabajador = models.ForeignKey(Trabajador)
    fecha_trabajo= models.DateTimeField('fecha_trabajo')
    descripcion = models.CharField(max_length=1000)
    horas_reales = models.FloatField()
    horas_cobrables = models.FloatField()

class Pieza(models.Model):
    coche = models.ForeignKey(Coche)
    nombre_pieza = models.CharField(max_length=200)
    precio = models.FloatField()
    fecha_entrada = models.DateTimeField('fecha_entrada_pieza')
