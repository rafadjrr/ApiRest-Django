"""API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url



urlpatterns = [
    path(r'^admin/', admin.site.urls),
    url(r'^helpcom/', include('apps.helpcom.urls')),
]"""
"""
#from django.urls import path
from rest_framework import routers
from apps.helpcom import viewsSets
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.conf import settings
from django.contrib import admin
from django.views.static import serve

router = routers.DefaultRouter()

router.register(r'area_de_conocimiento', viewsSets.AreaViewSet)
router.register(r'campaña', viewsSets.CampañaViewSet)
router.register(r'publicacion', viewsSets.PublicacionViewSet)
router.register(r'comentario', viewsSets.ComentarioViewSet)
router.register(r'PerfilUsuario', viewsSets.UsuariosViewSet)
router.register(r'user', viewsSets.UserViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(router.urls)),
    url(r'^autenticacion/', obtain_jwt_token),
    url(r'^registro/', include('rest_auth.registration.urls')),
    url(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT},),
    ]


"""


# prueba con industrial empieza aqui
from apps.helpcom import viewsSets
from django.urls import include, path
from django.conf.urls import url,include
from rest_framework import routers
from apps.industrialgip import views
from django.views.static import serve
from django.conf import settings
from django.contrib import admin


routeri = routers.DefaultRouter()
#routerh = routers.DefaultRouter()
# links para apps de industrial
routeri.register(r'users', views.UserViewSet)
routeri.register(r'groups', views.GroupViewSet)
routeri.register(r'empresa', views.EmpresaViewSet)
routeri.register(r'turno', views.TurnoViewSet)
routeri.register(r'Linea', views.LineaViewSet)
routeri.register(r'tp', views.TPViewSet)
routeri.register(r'turno', views.EmpresaViewSet)
routeri.register(r'materiaprima', views.MateriaPrimaViewSet)
routeri.register(r'planificacion', views.PlanificacionViewSet)
routeri.register(r'diarioprod', views.DiarioProdViewSet)
routeri.register(r'diariomp', views.DiarioMPViewSet)

#links para aplicacion red social
#routerh.register(r'area_de_conocimientoh', viewsSets.AreaViewSet)
#routerh.register(r'campañah', viewsSets.CampañaViewSet)
#routerh.register(r'publicacionh', viewsSets.PublicacionViewSet)
#routerh.register(r'comentarioh', viewsSets.ComentarioViewSet)
#routerh.register(r'PerfilUsuarioh', viewsSets.UsuariosViewSet)
#routerh.register(r'userh', viewsSets.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path(r'admin/', admin.site.urls),
   # path('helpcom/', include(routerh.urls)),
    path('industrialgip/', include(routeri.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT},),
    url(r'^registro/', include('rest_auth.registration.urls')),
]





