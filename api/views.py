from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import serializers
from .models import FaturamentoItem, ItemConfiguracao, Faturamento, FaturamentoItemConteudo

import datetime

# Create your views here.

@api_view(['GET'])
def apiOverview():
    return Response("API BASE POINT")

@api_view(['GET'])
def previa(request):
    faturamentoModel = Faturamento
    resultadoPrevia = faturamentoModel.objects.exclude(st_situacao='simulacao').order_by('-id')

    serializer = serializers.FaturamentoSerializer(resultadoPrevia, many=True)

    for previa in serializer.data:
        # Data_faturado - Formatação(Data/Hora) 
        data_hora = datetime.datetime.fromisoformat(previa['dt_faturado'][:-1])
        previa['dt_faturado'] = data_hora.strftime("%d/%m/%Y - %H:%M:%S")


    response = {'data': serializer.data, 'total': len(serializer.data)}
    return Response(response);

@api_view(['GET'])
def previaDetalhe(req, idPrevia):
    faturamentoItem_Model = FaturamentoItem

    previaDetalhe = faturamentoItem_Model.objects.filter(faturamento=idPrevia).order_by('item_configuracao')

    serializer = serializers.faturamento_itemSerializer(previaDetalhe, many=True)

    for item_faturamento in serializer.data:
        
        Item_configuracao = ItemConfiguracao.objects.filter(id = item_faturamento['item_configuracao']).order_by('camada_id__no_camada', 'no_item')

        for ic in Item_configuracao:

            item_faturamento['item_configuracao'] = { 
                'nome': ic.no_item, 
                'id': ic.id, 
                'classe': ic.classe.id,
                'nu_dia_regra_cobranca': ic.nu_dia_regra_cobranca, 
            }


    response = {'total': len(serializer.data), 'data': serializer.data}

    return Response(response)

@api_view(['GET'])
def itemConfiguracoesDetalhe(req, idConfig):
    faturamentoItemConteudo_Model = FaturamentoItemConteudo
    queryset = faturamentoItemConteudo_Model.objects.filter(faturamento_item_id = idConfig);

    serializer = serializers.faturamentoItemConteudo(queryset, many=True)

    data = serializer.data

    ics = data[0]['js_contabilizado']

    ics_nao_contabilizado = data[0]['js_nao_contabilizado']
    total_nao_contabilizado = len(ics_nao_contabilizado)

    icsCondicional = data[0]['js_condicional']
    totalCondicional = len(icsCondicional)

    icsDiversidade = data[0]['js_diversidade']
    totalDiversidade = len(icsDiversidade)

    data = {
        'total_contabilizado': len(ics),
        'contabilizado': ics ,

        "total_nao_contabilizado": total_nao_contabilizado, 
        "nao_contabilizado": ics_nao_contabilizado,

        'total_condicional': totalCondicional, 
        'condicional': icsCondicional, 

        'total_diversidade': totalDiversidade,
        'diversidade': icsDiversidade, 
        
    }

    return Response(data)