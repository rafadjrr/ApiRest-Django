from django.contrib import admin

# Register your models here
from .models import Empresa,TP,Linea,Turno,MateriaPrima,Planificacion,DiarioProd,DiarioMP
admin.site.site_header = "INDUSTRIAL GIP"
#admin.site.site_title = "Portal de industrial gip"
admin.site.index_title = "Bienvenidos al portal INDUSTRIAL GIP"

admin.site.register(Empresa)
admin.site.register(TP)
admin.site.register(Linea)
admin.site.register(Turno)

@admin.register(MateriaPrima)
class MateriaPrimaAdmin(admin.ModelAdmin):
    list_display = ('descripcion','empresadestino')

@admin.register(Planificacion)
class PlanificacionAdmin(admin.ModelAdmin):
    list_display = ('empresa','linea','tp','fecha', 'cantidadkg', 'estatus')

admin.site.register(DiarioProd)
admin.site.register(DiarioMP)
