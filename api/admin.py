from django.contrib import admin
from .models import *

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre_usuario", "correo")

class EstadoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")

class TareasAdmin(admin.ModelAdmin):
    list_display = ("id","tarea", "fecha_inicio", "fecha_fin", "descripcion", "usuario", "estado")

# Register your models here.
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Tareas, TareasAdmin)
