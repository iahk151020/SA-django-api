from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ecommerce.models import *

@api_view(['GET'])
def bookController(request):
    pass