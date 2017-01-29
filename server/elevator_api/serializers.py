from rest_framework import serializers
# from .models import booksmodel,contents, ownermodel,carmodel
from .models import  ownermodel,carmodel

# class contentserializer(serializers.ModelSerializer):

# 	class Meta:
# 		model =contents
# 		fields ='__all__'


# class booksserializer(serializers.ModelSerializer):
#     # stories = serializers.StringRelatedField(many=True)
#     stories = contentserializer(many=True)


#     class Meta:
#         model = booksmodel
#         fields =('id','title', 'cover','n_likes','like', 'stories')


# my elevator data
class ownerserializer(serializers.ModelSerializer):
    
	class Meta:
		model =ownermodel
		fields ='__all__'



class carserializer(serializers.ModelSerializer):
    # stories = serializers.StringRelatedField(many=True)
    stories = ownerserializer(many=True)


    class Meta:
        model = carmodel
        fields =('id','owner', 'plateno','model', 'stories')
