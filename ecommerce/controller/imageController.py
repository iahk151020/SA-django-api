from rest_framework import generics
from rest_framework.response import Response
from ecommerce.imageRender import JPEGRenderer
from ecommerce.models import Item

class ImageAPIView(generics.RetrieveAPIView):
    renderer_classes = [JPEGRenderer]
    
    def get(self, request, *args, **kwargs):
        queryset = Item.objects.get(id=self.kwargs['id']).image 
        return Response(queryset, content_type='image/jpg')