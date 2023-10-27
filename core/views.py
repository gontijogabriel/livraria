from rest_framework.viewsets import ModelViewSet
from drf_yasg import openapi

from core.serializers import (
    CategoriaSerializer, 
    EditoraSerializer, 
    AutorSerializer,
    LivroSerializer,
    LivroDetailSerializer,
    CompraSerializer,
    ItensCompraSerializer
)
from core.models import ( 
    Categoria, 
    Editora, 
    Autor,
    Livro,
    Compra,
    ItensCompra
)

class CategoriaViewSet(ModelViewSet):
    """Categoria"""
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class EditoraViewSet(ModelViewSet):
    """Editora"""
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

class AutorViewSet(ModelViewSet):
    """Autor"""
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LivroViewSet(ModelViewSet):
    """Livro"""
    queryset = Livro.objects.all()
    
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return LivroDetailSerializer

        return LivroSerializer

class CompraViewSet(ModelViewSet):
    """Compra"""
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer


class ItensCompraViewSet(ModelViewSet):
    """Compra"""
    queryset = ItensCompra.objects.all()
    serializer_class = ItensCompraSerializer