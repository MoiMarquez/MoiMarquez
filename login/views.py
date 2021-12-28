from django.http import response
from rest_framework import status, views
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def moi(request):
    if request.method == 'GET':
        name= 'moiiii'
        return Response({'message': f'{name} este es tu primer metodo en Django'})