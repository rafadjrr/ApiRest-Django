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