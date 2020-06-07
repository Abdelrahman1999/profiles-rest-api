from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers



class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is similar to a traditional django view',
            'Gives you you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})


    def post(self, request):
        """Create a hello message with our name """
        serializer = self.serializer_class(data=request.data)

        if (serializer.is_valid()):
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
             )


    #replacing an object with the object being provided and for updating an entire object
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    #only updates the fields provided in the requests
    def patch(self,request, pk=None):
        """Handle partial update of an object"""
        return Response({'method': 'PATCH'})

    #deletes an object in the database
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
