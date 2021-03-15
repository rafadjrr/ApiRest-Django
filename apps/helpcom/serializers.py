from rest_framework import serializers
from .models import Publicacion,Usuario,Comentario,Campaña,AreaDeConocimiento
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AreaDeConocimiento
        fields = ('__all__')


class PublicacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publicacion
        fields = ('__all__')
        
class PublicacionListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publicacion
        fields = ('__all__')
        #ordering=('id_publicacion') 

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')

class ComentarioListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comentario
        fields=('id_comentario','id_usuario','id_publicacion','contenido','fecha')
        

class ComentarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comentario
        fields = ('__all__')        

class CampañasListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Campaña
        fields = ('id_campaña','id_usuario','objetivo','foto')
         

class CampañaSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Campaña
        fields = ('__all__')

