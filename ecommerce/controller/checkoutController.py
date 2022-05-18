from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ecommerce.dao.cartDAO import *
from ..dao.productDAO import *

@api_view(['GET'])
def handleGetCurrentCart(request):
    customerId = request.GET.get('customerId')
    print('customer id:', customerId)
    res = getCurrentCart(int(customerId))
    return JsonResponse(res, safe=False)

@api_view(['POST'])
def handleAddToCart(request): 
    data = request.data
    customerId = data['customerId']
    itemId = data['itemId']
    quantity = data['quantity']
    addToCart(customerId, quantity, itemId)
    return Response("Added to cart successfully", status=200)

@api_view(['DELETE'])
def handleRemoveFromCart(request): 
    data = request.data
    customerId = data['customerId']
    itemId = data['itemId']
    removeFromCart(customerId, itemId)
    return Response("Successfully removing item from cart", status=200)

@api_view(['POST'])
def handleUpdateCartItemQuantity(request): 
    data = request.data
    customerId = data['customerId']
    itemId = data['itemId']
    quantity = data['quantity']
    updateCartItemQuantity(customerId, itemId, quantity)
    return Response("Successfully updating cart item quantity", status=200)

@api_view(['PUT'])
def handleClickCheckout(request): 
    data = request.data
    customerId = data['customerId']
    items = data['items']
    res = clickCheckout(customerId, items)
    return JsonResponse(res, safe=False)