
from __future__ import unicode_literals
from rest_framework import permissions
from rest_framework.response import Response
#from rest_framework.decorators import detail_route
from rest_framework import viewsets, status
from .models import Usuario,Publicacion,Comentario,Campaña,AreaDeConocimiento,Like,Seguidor
from .serializers import(AreaSerializer, UserSerializer,UsuariosSerializer,CampañasListSerializer,
CampañaSerializer,PublicacionListSerializer,PublicacionSerializer,ComentarioListSerializer,ComentarioSerializer)
from django.contrib.auth.models import User

class AreaViewSet(viewsets.ModelViewSet):
    queryset = AreaDeConocimiento.objects.all()
    serializer_class = AreaSerializer

class PublicacionViewSet(viewsets.ModelViewSet):
    
    queryset = Publicacion.objects.all().order_by('-fecha_publ')
    serializer_class = PublicacionSerializer


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuariosSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ComentarioList(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioListSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class campañasList(viewsets.ModelViewSet):
    queryset = Campaña.objects.all()
    serializer_class = CampañasListSerializer

class CampañaViewSet(viewsets.ModelViewSet):
    queryset = Campaña.objects.all()
    serializer_class = CampañaSerializer
   
