#serializer: it is a feature in django that easily converts data inputs to python objects and vice versa
#for POST and UPDATE to recieve content that we post to the api
from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)
    
