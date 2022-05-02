from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..dao.productDAO import *

@api_view(['POST'])
def submitOrder(request):
    pass    
