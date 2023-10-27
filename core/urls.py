from django.urls import path, include
from core import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categoria', views.CategoriaViewSet)
router.register(r'editora', views.EditoraViewSet)
router.register(r'autor', views.AutorViewSet)
router.register(r'livros', views.LivroViewSet)
router.register(r'compra', views.CompraViewSet)
router.register(r'itens-compra', views.ItensCompraViewSet)
router.register(r'usuario', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]