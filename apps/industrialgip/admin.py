from django.contrib import admin

# Register your models here
from .models import Empresa,TP,Linea,Turno,MateriaPrima,Planificacion,DiarioProd,DiarioMP


admin.site.register(Empresa)
admin.site.register(TP)
admin.site.register(Linea)
admin.site.register(Turno)
admin.site.register(MateriaPrima)
admin.site.register(Planificacion)
admin.site.register(DiarioProd)
admin.site.register(DiarioMP)
