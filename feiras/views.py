from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from feiras.models import Feira
from feiras.serializers import FeiraSerializer

@api_view(['GET', 'POST'])
def feira_list(request):
    """
    List all feira data stored, or create a new feira.
    """
    if request.method == 'GET':
        feiras = Feira.objects.all()
        serializer = FeiraSerializer(feiras, many=True)

        return Response(serializer.data)
        

    elif request.method == 'POST':
        
        serializer = FeiraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def feira_detail(request, pk):

    """
    Retrieve, update or delete a feira data.
    """
    try:
        feira = Feira.objects.get(pk=pk)
    except Feira.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FeiraSerializer(feira)
        return Response(serializer.data)

    elif request.method == 'PUT':
        
        serializer = FeiraSerializer(feira, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        feira.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



