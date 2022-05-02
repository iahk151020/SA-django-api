from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from ..dao.productDAO import *

@api_view(['GET'])
def handleGetAllProductItems(request):
    
    page = request.GET.get('page')
    limit = request.GET.get('limit')
    res = getAllProductItems(int(page), int(limit))
    return JsonResponse(res, safe=False)

@api_view(['GET'])
def handleGetAllBookItems(request):
    
    page = request.GET.get('page')
    limit = request.GET.get('limit')
    res = getAllBookItems(int(page), int(limit))
    return JsonResponse(res, safe=False)

@api_view(['GET'])
def handleGetAllLaptopItems(request):
    
    page = request.GET.get('page')
    limit = request.GET.get('limit')
    res = getAllLaptopItems(int(page), int(limit))
    return JsonResponse(res, safe=False)

@api_view(['GET'])
def handleGetAllClothesItems(request):
    
    page = request.GET.get('page')
    limit = request.GET.get('limit')
    res = getAllClothesItems(int(page), int(limit))
    return JsonResponse(res, safe=False)

@api_view(['GET'])
def handleGetAllMobileItems(request):
    
    page = request.GET.get('page')
    limit = request.GET.get('limit')
    res = getAllMobileItems(int(page), int(limit))
    return JsonResponse(res, safe=False)

@api_view(['GET'])
def handleGetAllElectronicsItems(request):
    
    page = request.GET.get('page')
    limit = request.GET.get('limit')
    res = getAllElectronicsItems(int(page), int(limit))
    return JsonResponse(res, safe=False)

@api_view(['GET'])
def handleGetProductItemByName(request): 
    name = request.GET.get('name')
    res = getProductItemByName(name)
    return JsonResponse(res, safe=False)

@api_view(['GET'])
def handleGetLaptopBrands(request):
    res = getLaptopBrands()
    return JsonResponse(res, safe=False)

@api_view(['GET'])
def handleGetMobileBrands(request):
    res = getMobileBrands()
    return JsonResponse(res, safe=False)

@api_view(['GET'])
def handleGetElectronicsBrands(request):
    res = getElectronicsBrands()
    return JsonResponse(res, safe=False)

@api_view(['GET'])
def handleGetClothesBrands(request):
    res = getClothesBrands()
    return JsonResponse(res, safe=False)

@api_view(['GET'])
def handleGetItemDetails(request): 
    id = request.GET.get('id')
    type = request.GET.get('type')
    res = getItemDetails(id, type)
    if res is not None: 
        return JsonResponse(res, safe=False)
    else: 
        return Response(status=404)