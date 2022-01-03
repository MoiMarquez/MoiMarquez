from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers

@api_view(['GET'])
def moi(request):
    if request.method == 'GET':
        name= 'moiiii'
        return Response({'message': f'{name} este es tu primer metodo en Django'})

@api_view(['GET', 'POST'])
def appjson(request):
    if request.method == 'GET':
        user = models.User.objects.all()
        serializer = serializers.UsersSerializer(user,many=True)
        return Response({"result":serializer.data})
