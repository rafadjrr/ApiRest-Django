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
    list_display = ('id','empresa','linea','tp','fecha', 'cantidadkg', 'estatus')
    ordering = ('-fecha',)
    search_fields = ('empresa__descripcion','linea__descripcion','tp__descripcion','estatus','fecha','cantidadkg')
    list_display_links = ('id','empresa','linea','tp','fecha', 'cantidadkg', 'estatus')
    list_filter = ('id','empresa','linea','tp','fecha', 'cantidadkg', 'estatus')
    list_per_page = 10

@admin.register(DiarioProd)
class DiarioProdAdmin(admin.ModelAdmin):
    list_display = ('orden','turno','fecha','hora', 'kilosp', 'desperdicios','idrack','observaciones')
    ordering = ('-fecha',)
#    search_fields = ('orden__id','turno__descripcion','fecha','cantidadkg','idrack','observaciones')
    list_display_links = ('orden','turno','fecha','hora', 'kilosp', 'desperdicios','idrack','observaciones')

    list_filter = ('orden','turno','fecha','hora', 'kilosp', 'desperdicios','idrack','observaciones')
    list_per_page = 10
#admin.site.register(DiarioProd)

@admin.register(DiarioMP)
class DiarioMPAdmin(admin.ModelAdmin):
    list_display = ('turno','linea','producto','materiaprima', 'fecha', 'ingresokg','consumokg','observaciones')
#admin.site.register(DiarioMP)
