from rest_framework import serializers
from .models import booksmodel


class booksserializer(serializers.ModelSerializer):

	class Meta:
		model = booksmodel
		# fields =('name','lecture', 'dept','day')
		fields ='__all__'

