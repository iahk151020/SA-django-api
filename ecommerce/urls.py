from django.urls import path
from . import views
from .controller.accountController import *
from .controller.bookController import *
from .controller.imageController import ImageAPIView

urlpatterns = [
    path('account/', accountController, name='account'),
    path('book/', bookController, name='book'),
    path('image/<id>', ImageAPIView.as_view()),
]
