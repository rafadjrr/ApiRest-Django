from __future__ import unicode_literals
# Create your models here
from django.db import models
import datetime

class Empresa(models.Model):
    descripcion = models.CharField(max_length=50)
    def __str__(self):
        return self.descripcion

class TP(models.Model):
    descripcion = models.CharField(max_length=50)
    def __str__(self):
        return self.descripcion

class Linea(models.Model):
    descripcion = models.CharField(max_length=50)
    def __str__(self):
        return self.descripcion

class Turno(models.Model):
    descripcion = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)
    def __str__(self):
        texto = "{0} {1}"
        return texto.format(self.descripcion, self.horario)
        

class MateriaPrima(models.Model):
    descripcion = models.TextField()
    empresadestino = models.ForeignKey(Empresa,related_name='MpE',null=True,blank=True,on_delete=models.CASCADE)


class Planificacion(models.Model):
    empresa = models.ForeignKey(Empresa,related_name='PlE',null=True,blank=True,on_delete=models.CASCADE)
    linea = models.ForeignKey(Linea,null=True,related_name='PlL',blank=True,on_delete=models.CASCADE)
    tp = models.ForeignKey(TP ,related_name='PlTp',null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default = datetime.datetime.now)
    cantidadkg = models.FloatField()
    estatus = models.CharField(max_length=5)
    def __str__(self):
        texto = "{0} {1} {2} kg:{3}"
        return texto.format(self.empresa, self.linea, self.fecha, self.cantidadkg)

class DiarioProd(models.Model):
    orden = models.OneToOneField(Planificacion, related_name='DpO', on_delete=models.CASCADE)
    turno = models.ForeignKey(Turno,null=True,related_name='DpT',blank=True,on_delete=models.CASCADE)
    fecha =  models.DateTimeField(default = datetime.datetime.now)
    hora = models.TimeField()
    kilosp = models.FloatField()
    desperdicios = models.IntegerField()
    idrack = models.IntegerField()
    observaciones = models.CharField(max_length=50)

class DiarioMP(models.Model):
    turno = models.ForeignKey(Turno,related_name='DmpT',null=True,blank=True,on_delete=models.CASCADE)
    linea = models.ForeignKey(Linea,related_name='DmpL',null=True,blank=True,on_delete=models.CASCADE)
    producto = models.ForeignKey(Planificacion,related_name='DmpP',null=True,blank=True,on_delete=models.CASCADE)
    materiaprima = models.ForeignKey(MateriaPrima,related_name='DmpMt',null=True,blank=True,on_delete=models.CASCADE)
    fecha = models.DateTimeField(default = datetime.datetime.now)
    ingresokg = models.FloatField()
    consumokg = models.FloatField()
    observaciones = models.TextField()
