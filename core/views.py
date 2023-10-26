from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_list_or_404
from core.models import Categoria
from django.views import View
import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from core.serializers import CategoriaSerializer
from drf_yasg import openapi

    
class CategoriasList(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('filtro', openapi.IN_QUERY, type=openapi.TYPE_STRING, description='Filtro para categorias', request_body=True)
        ]
    )
    def get(self, request):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        seralizer = CategoriaSerializer(data=request.data)
        if seralizer.is_valid():
            seralizer.save()
            return Response(seralizer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(seralizer.error, status=status.HTTP_400_BAD_REQUEST)
        

class CategoriaDetail(APIView):
    def get(self,request, id):
        query_set = Categoria.objects.get(id=id)
        data = {}
        data['id'] = query_set.id
        data['descricao'] = query_set.descricao
        return JsonResponse(data)
    