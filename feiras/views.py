from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from feiras.models import Feira
from feiras.serializers import FeiraSerializer

@csrf_exempt
def feira_list(request):
    """
    List all feira data stored, or create a new feira.
    """
    if request.method == 'GET':
        feiras = Feira.objects.all()
        serializer = FeiraSerializer(feiras, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FeiraSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def feira_detail(request, pk):

    """
    Retrieve, update or delete a feira data.
    """
    try:
        feira = Feira.objects.get(pk=pk)
    except Feira.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = FeiraSerializer(feira)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FeiraSerializer(feira, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        feira.delete()
        return HttpResponse(status=204)



