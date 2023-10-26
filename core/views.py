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
from core.serializers import CategoriasSerializer

@method_decorator(csrf_exempt, name="dispatch")
class CategoriaView(View):
    def get(self, request, id=None):
        if id:
            query_set = Categoria.objects.get(id=id)
            data = {}
            data['id'] = query_set.id
            data['descricao'] = query_set.descricao
            return JsonResponse(data)
        
        else:
            data = list(Categoria.objects.values())
            formatted_data = json.dumps(data, ensure_ascii=False)
            return HttpResponse(formatted_data, content_type="application/json")
    
    def post(self, request):
        json_data = json.loads(request.body)
        nova_categoria = Categoria.objects.create(**json_data)
        data = {"id": nova_categoria.id, "descricao": nova_categoria.descricao}
        return JsonResponse(data)
    
    def patch(self, request, id):
        json_data = json.loads(request.body)
        query_set = Categoria.objects.get(id=id)
        query_set = json_data['descricao'] if 'descricao' in json_data else query_set.descricao
        query_set.save()
        data = {}
        data['id'] = query_set.index
        data['descricao'] = query_set.descricao
        return  JsonResponse(data)
    
    def delete(self, request, id):
        query_set = Categoria.objects.get(id=id)
        query_set.delete()
        data = {'mensagem': "Item deletado!"}
        return JsonResponse(data)
    
    
class CategoriasList(APIView):
    def get(self, request):
        categorias = Categoria.objects.all()
        serializer = CategoriasSerializer(categorias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        seralizer = CategoriasSerializer(data=request.data)
        if seralizer.is_valid():
            seralizer.save()
            return Response(seralizer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(seralizer.error, status=status.HTTP_400_BAD_REQUEST)
        

class CategoriaDetail(APIView):
    def get(self,request, id):
        #categoria = get_list_or_404(Categoria.objects.all(), id=id)
        categoria = get_list_or_404(Categoria, id=id)
        serializer = CategoriasSerializer(categoria)
        return Response(serializer.data)
        