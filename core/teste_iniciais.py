from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class CategoriasList(APIView):
    def get(self, request):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'descricao': openapi.Schema(type=openapi.TYPE_STRING, description='Descrição da categoria')
            }
        )
    )
    def post(self, request):
        data = request.data
        descricao = data.get('descricao')
        
        # Verifica se já existe uma categoria com a mesma descrição
        if Categoria.objects.filter(descricao=descricao).exists():
            return Response({'error': 'Categoria com a mesma descrição já existe.'}, status=status.HTTP_400_BAD_REQUEST)
        
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
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('id', openapi.IN_PATH, type=openapi.TYPE_INTEGER, description='ID da categoria a ser atualizada')
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'descricao': openapi.Schema(type=openapi.TYPE_STRING, description='Nova descrição da categoria')
            }
        ),
        responses={
            200: openapi.Response('Categoria atualizada com sucesso', CategoriaSerializer),
            400: 'Erro na solicitação',
            404: 'Categoria não encontrada'
        }
    )
    def put(self, request, id):
        categoria = Categoria.objects.get(id=id)
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        categoria = Categoria.objects.get(id=id)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class CategoriaListGeneric(ListCreateAPIView):
    """ListCreateAPIView"""
    # Obrigatorio = quertset e seralizer_class
    quertset = Categoria.objects.all()
    seralizer_class = CategoriaSerializer


class CategoriaDetailGeneric(RetrieveUpdateDestroyAPIView):
    """RetrieveUpdateDestroyAPIView"""
    lookup_field = 'id' # seta o campo de busca
    quertset = Categoria.objects.all()
    seralizer_class = CategoriaSerializer