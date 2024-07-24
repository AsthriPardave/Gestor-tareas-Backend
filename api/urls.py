from django.urls import path, include
from .models import *
from rest_framework import routers, serializers, viewsets

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__" 

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = "__all__" 

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class TareasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tareas
        fields = "__all__" 

class TareasViewSet(viewsets.ModelViewSet):
    queryset = Tareas.objects.all()
    serializer_class = TareasSerializer

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'estados', EstadoViewSet)
router.register(r'tareas', TareasViewSet)

urlpatterns = [
    path('', include(router.urls)),
]