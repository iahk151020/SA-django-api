from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ecommerce.models import *

@api_view(['GET'])
def bookController(request):
    book1 = Book.objects.get(id=4)
    res = {
        'id': book1.id,
        'name': book1.name,
        'price': book1.price,
        'page': book1.page,
        'image': 'localhost:8000/api/v1/image/' + str(book1.id),

    }
    return JsonResponse(res, safe=False)