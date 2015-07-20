# -*- coding: utf-8 -*-
from django.db import models

class Coches(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=200)
    matricula = models.CharField(max_length=25)
    fecha_entrada= models.DateTimeField('fecha_entrada')
    fecha_salida= models.DateTimeField('fecha_salida')
    descripcion_averia = models.CharField(max_length=1000)
    def __str__(self):
        return self.matricula

    class Meta:
        verbose_name_plural = "Coches"
        verbose_name = "Coche"




class Trabajadores(models.Model):
    dni = models.CharField(max_length=9)
    #anadimos el campo DNI para que no se pisen los nombres
    nombre = models.CharField(max_length=50)
    sueldo_hora = models.FloatField()
    #es el estipulado en el contrato no el que producen según la aplicacion

    class Meta:
        verbose_name_plural = "Trabajadores"
        verbose_name = "Trabajadores"


class Piezas(models.Model):
    coche = models.ForeignKey(Coches)
    nombre_pieza = models.CharField(max_length=200)
    precio = models.FloatField()
    fecha_entrada = models.DateTimeField('fecha_entrada_pieza')

    class Meta:
        verbose_name_plural = "Piezas"
        verbose_name = "Piezas"



class Trabajos(models.Model):
    coche = models.ForeignKey(Coches)
    trabajador = models.ForeignKey(Trabajadores)
    pieza = models.ForeignKey(Piezas)
    fecha_trabajo= models.DateTimeField('fecha_trabajo')
    descripcion = models.CharField(max_length=1000)
    hora_inicio = models.TimeField()
    hora_final = models.TimeField()

    class Meta:
        verbose_name_plural = "Trabajos"
        verbose_name = "Trabajos"
#El eje central de la aplicacion son los trabajos, es un trabajo/tarea


class Proveedores(models.Model):
    cif = models.CharField(max_length = 9)
    nombreempresa = models.CharField(max_length = 200)
    direccion = models.CharField(max_length = 200)
    telefono = models.IntegerField()

    class Meta:
        verbose_name_plural = "Proveedores"
        verbose_name = "Proveedores"
    # Añadimos proveedores con la infomacion  necesaria de cada uno de ellos
