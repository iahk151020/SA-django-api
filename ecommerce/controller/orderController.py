from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from ..dao.orderDAO import *

@api_view(['POST'])
def handleCreateOrder(request): 
    data = request.data
    customerId = data['customerId']
    paymentType = data['payment_type']
    shipmentType = data['shipment_type']
    totalPrice = data['total_price']
    res = createOrder(customerId, paymentType, shipmentType, totalPrice)
    return JsonResponse(res, safe=False)