from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework import viewsets
from apps.industrialgip.models import Empresa, TP, Linea, Turno, MateriaPrima, Planificacion, DiarioProd, DiarioMP
from apps.industrialgip.serializers import UserSerializer, GroupSerializer, EmpresaSerializer, TPSerializer, LineaSerializer, TurnoSerializer, MateriaPrimaSerializer, PlanificacionSerializer, DiarioProdSerializer, DiarioMPSerializer
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hellow, welcome to the jungle. this is DJANGO /admin ----> admin site")

# create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmpresaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [permissions.IsAuthenticated]

class TPViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = TP.objects.all()
    serializer_class = TPSerializer
    permission_classes = [permissions.IsAuthenticated]

class LineaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Linea.objects.all()
    serializer_class = LineaSerializer
    permission_classes = [permissions.IsAuthenticated]

class TurnoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer
    permission_classes = [permissions.IsAuthenticated]

class MateriaPrimaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = MateriaPrima.objects.all()
    serializer_class = MateriaPrimaSerializer
    permission_classes = [permissions.IsAuthenticated]

class PlanificacionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Planificacion.objects.all()
    serializer_class = PlanificacionSerializer
    permission_classes = [permissions.IsAuthenticated]

class DiarioProdViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = DiarioProd.objects.all()
    serializer_class = DiarioProdSerializer
    permission_classes = [permissions.IsAuthenticated]

class DiarioMPViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = DiarioMP.objects.all()
    serializer_class = DiarioMPSerializer
    permission_classes = [permissions.IsAuthenticated]
