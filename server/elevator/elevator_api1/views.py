from .models import booksmodel
from .serializers import booksserializer 
from rest_framework.views import APIView 
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets 


class books(APIView):
    def get(self, request):
        books= booksmodel.objects.all()
        serializer=booksserializer(books, many=True)
        return Response(serializer.data)
        

    def post(self):
        pass



class booksViewSet(viewsets.ModelViewSet):
	
	# metadata_class = APIRootMetadata
	queryset = booksmodel.objects.all()
	serializer_class = booksserializer
