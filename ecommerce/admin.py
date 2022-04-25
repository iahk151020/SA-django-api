from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Account)
admin.site.register(Address)
admin.site.register(FullName)
admin.site.register(Customer)
admin.site.register(Comment)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(Item)