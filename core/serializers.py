from rest_framework import serializers
from core.models import Categoria, Editora, Autor, Livro, Compra, ItensCompra
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        depth = 1


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        

class EditoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'


# Detail
class LivroDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
        depth = 1


class CompraSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    
    class Meta:
        model = Compra
        fields = '__all__'
        
    def get_status(self, instance):
        return instance.get_status_display()
        

# Detail
# class CompraDetailSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Compra
#        fields = '__all__'
#        depth = 1


class ItensCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = '__all__'


# Detail
class ItensCompraDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = '__all__'
        depth = 1
        