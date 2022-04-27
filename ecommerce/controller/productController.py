from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from ..dao.productDAO import *

@api_view(['GET'])
def handleGetAllProducts(request):
    
    page = request.GET.get('page')
    limit = request.GET.get('limit')
    res = getAllProducts(int(page), int(limit))
    return JsonResponse(res, safe=False)