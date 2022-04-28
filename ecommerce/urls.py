from django.urls import path
from . import views
from .controller.accountController import *
from .controller.bookController import *
from .controller.imageController import *
from .controller.productController import *

urlpatterns = [
    path('login', login),
    path('products', handleGetAllProductItems),
    path('products/books', handleGetAllBookItems),
    path('products/laptops', handleGetAllLaptopItems),
    path('products/clothes', handleGetAllClothesItems),
    path('products/mobiles', handleGetAllMobileItems),
    path('products/electronics', handleGetAllElectronicsItems),
    path('products-by-name', handleGetProductItemByName),
    path('laptop-brands', handleGetLaptopBrands),
    path('mobile-brands', handleGetMobileBrands),
    path('clothes-brands', handleGetClothesBrands),
    path('electronics-brands', handleGetElectronicsBrands),
    path('item-detail', handleGetItemDetails),
    path('image/book/<id>', bookImageAPI.as_view()),
    path('image/laptop/<id>', laptopImageAPI.as_view()),
    path('image/clothes/<id>', clothesImageAPI.as_view()),
    path('image/mobile/<id>', mobileImageAPI.as_view()),
    path('image/electronics/<id>', electronicsImageAPI.as_view()),
]
