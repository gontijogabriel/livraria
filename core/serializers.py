
from rest_framework import serializers
from core.models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    descricao = serializers.CharField()
    class Meta:
        model = Categoria
        fields = '__all__'