from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import FaturamentoSerializer
from .models import Faturamento

from . import helpers

# Create your views here.

@api_view(['GET'])
def apiOverview(req):
    return Response("API BASE POINT")

@api_view(['GET'])
def previa(request):
    resultadoPrevia = Faturamento.objects.all()
    previasSemSimulacao = []
    for previa in resultadoPrevia:
        if previa.st_situacao != 'simulacao':
            previasSemSimulacao.append(previa)
    
    helpers.orderListByDescrent(previasSemSimulacao)

    serializer = FaturamentoSerializer(previasSemSimulacao, many=True)
    response = {'data': serializer.data, 'total': len(serializer.data)}
    return Response(response);
