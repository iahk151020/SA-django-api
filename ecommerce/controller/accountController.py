from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from ..dao.accountDao import *

@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)
    username = data['username']
    password = data['password']
    res = checkLogin(username, password)

    if res is False: 
        return Response(status=400)
        
    return JsonResponse(res, safe=False)