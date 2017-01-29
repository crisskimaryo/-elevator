from django.shortcuts import render

# from .models import booksmodel, contents,carmodel,ownermodel
# from .serializers import booksserializer , contentserializer,carserializer,ownerserializer

from .models import carmodel,ownermodel
from .serializers import carserializer,ownerserializer
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import viewsets
# from drf_multiple_model.views import MultipleModelAPIView , MultipleModelViewSet




class cars(APIView):
    def get(self, request):
        books= carmodel.objects.filter(pk=1)
        content=ownermodel.objects.all()
        book=carserializer(books, many=True)
        content=ownerserializer(content, many=True)
        return Response({
        'book': book.data,
        'content': content.data,
    })

    def get_content(self):
        b=ownermodel.objects.filter(pk=1)
        return b




    def post(self):
        pass

# class books(APIView):
#     def get(self, request):
#         books= booksmodel.objects.filter(pk=1)
#         content=contents.objects.all()
#         book=carserializer(books, many=True)
#         content=contentserializer(content, many=True)
#         return Response({
#         'book': book.data,
#         'content': content.data,
#     })

#     def get_content(self):
#         b=contents.objects.filter(pk=1)
#         return b




#     def post(self):
#         pass



# class booksViewSet(viewsets.ModelViewSet):
# 	queryset = booksmodel.objects.all()
# 	serializer_class = booksserializer




class carsViewSet(viewsets.ModelViewSet):
	queryset = carmodel.objects.all()
	serializer_class = carserializer