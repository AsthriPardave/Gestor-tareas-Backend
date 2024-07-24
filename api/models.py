from django.db import models

# Create your models here.
class Usuario(models.Model):
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)
    nombre_usuario = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.nombre_usuario

class Estado(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre

class Tareas(models.Model):
    tarea = models.CharField(max_length=100)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    descripcion = models.CharField(max_length=500)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)