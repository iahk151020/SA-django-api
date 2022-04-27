from rest_framework import generics
from rest_framework.response import Response
from ecommerce.imageRender import JPEGRenderer, PNGRender
from ecommerce.models import Book, Laptop, Clothes, Mobile, Electronics

class bookImageAPI(generics.RetrieveAPIView):
    renderer_classes = [JPEGRenderer, PNGRender]
    
    def get(self, request, *args, **kwargs):
        queryset = Book.objects.get(id=self.kwargs['id']).image 
        return Response(queryset, content_type='image/jpg')

class laptopImageAPI(generics.RetrieveAPIView):
    renderer_classes = [JPEGRenderer, PNGRender]
    
    def get(self, request, *args, **kwargs):
        queryset = Laptop.objects.get(id=self.kwargs['id']).image 
        return Response(queryset, content_type='image/jpg')

class clothesImageAPI(generics.RetrieveAPIView):
    renderer_classes = [JPEGRenderer, PNGRender]
    
    def get(self, request, *args, **kwargs):
        queryset = Clothes.objects.get(id=self.kwargs['id']).image 
        return Response(queryset, content_type='image/jpg')

class mobileImageAPI(generics.RetrieveAPIView):
    renderer_classes = [JPEGRenderer, PNGRender]
    
    def get(self, request, *args, **kwargs):
        queryset =Mobile.objects.get(id=self.kwargs['id']).image 
        return Response(queryset, content_type='image/jpg')

class electronicsImageAPI(generics.RetrieveAPIView):
    renderer_classes = [JPEGRenderer, PNGRender]
    
    def get(self, request, *args, **kwargs):
        queryset = Electronics.objects.get(id=self.kwargs['id']).image 
        return Response(queryset, content_type='image/jpg')
