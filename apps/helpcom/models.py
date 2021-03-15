from __future__ import unicode_literals
from django.db import models
import datetime
from django.contrib.auth.models import User

class AreaDeConocimiento(models.Model):
    descripcion = models.TextField()

 
class Usuario(models.Model):
    user = models.OneToOneField(User, related_name='persona', on_delete=models.CASCADE)
    nombre     = models.CharField(max_length=50)
    apellido  = models.CharField(max_length=60)
    area = models.ManyToManyField(AreaDeConocimiento)
    avatar = models.ImageField(upload_to='fotos_perfil')
    info = models.TextField()
    estado = models.TextField()
    seguir = models.BigIntegerField()

class Campaña(models.Model):
    usuario = models.ForeignKey(Usuario,null=True,blank=True,on_delete=models.CASCADE)
    objetivo    = models.TextField()
    foto           = models.ImageField(upload_to='fotos_campaña')
    meta       = models.TextField()
    fechaCulminacion = models.DateTimeField(default = datetime.datetime.now)
    clasificacion = models.DecimalField(blank=True, max_digits=5, decimal_places=2)

class Publicacion(models.Model):
    usuario = models.ForeignKey(Usuario,null=True,blank=True,on_delete=models.CASCADE)
    descripcion    = models.TextField()
    fecha_publ     = models.DateTimeField(default = datetime.datetime.now,blank=True,null=True)
    foto           = models.ImageField(upload_to='fotos_publicacion',blank=True,null=True)
    campaña = models.ForeignKey(Campaña,null=True,blank=True,on_delete=models.CASCADE)
    area = models.TextField(blank=True,null=True)
    megusta = models.BigIntegerField(blank=True,null=True)
   
class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario,null=True,blank=True,on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion,null=True,blank=True,on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(default = datetime.datetime.now)

class Like(models.Model):
    usuario = models.ForeignKey(Usuario,null=True,blank=True,on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion,null=True,blank=True,on_delete=models.CASCADE)

class Seguidor(models.Model):
    usuario = models.ForeignKey(Usuario,null=True,blank=True,on_delete=models.CASCADE)
    campaña = models.ForeignKey(Campaña,null=True,blank=True,on_delete=models.CASCADE)
