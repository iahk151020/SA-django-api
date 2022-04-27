from django.urls import path
from . import views
from .controller.accountController import *
from .controller.bookController import *
from .controller.imageController import *
from .controller.productController import *

urlpatterns = [
    path('login', login),
    path('products', handleGetAllProductItems),
    path('image/book/<id>', bookImageAPI.as_view()),
    path('image/laptop/<id>', laptopImageAPI.as_view()),
    path('image/clothes/<id>', clothesImageAPI.as_view()),
    path('image/mobile/<id>', mobileImageAPI.as_view()),
    path('image/electronics/<id>', electronicsImageAPI.as_view()),
]
