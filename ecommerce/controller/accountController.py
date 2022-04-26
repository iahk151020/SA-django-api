from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ecommerce.models import *

@api_view(['GET'])
def accountController(request):
    account1 = Account.objects.get(id = 1)
    customer1 = account1.customerId
    print(customer1)
    res = {
        'id': account1.id,
        'username': account1.username,
        'password': account1.password,
        'customer': {
            'id': customer1.id,
            'phone': customer1.phone,
            'email': customer1.email,
            'dob': customer1.dob,
        }
    }
    return JsonResponse(res, safe=False)