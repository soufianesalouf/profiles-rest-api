from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class helloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""

        an_apiview = [
        'Uses HTTP methods as function (get, post, put, patch, delete)',
        'Is similar to a traditional django view',
        'Gives you the most control over your application logic',
        'Is mapped manually to URLs',
        ]

        return Response({'massage': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'massage': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({'Method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of an object"""

        return Response({'Method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'Method': 'Delete'})
