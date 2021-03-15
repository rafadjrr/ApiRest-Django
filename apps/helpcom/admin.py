from django.contrib import admin
# Register your models here.
from .models import Usuario, Publicacion,Campaña,Comentario,Like,Seguidor,AreaDeConocimiento


admin.site.register(Usuario)
admin.site.register(Publicacion)
admin.site.register(Campaña)
admin.site.register(Comentario)
admin.site.register(Like)
admin.site.register(Seguidor)
admin.site.register(AreaDeConocimiento)