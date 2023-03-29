from rest_framework import serializers
from . import models

class FaturamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Faturamento
        fields ='__all__'

class faturamento_itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FaturamentoItem
        fields = '__all__'
class itemConfiguracao(serializers.ModelSerializer):
    class Meta:
        model = models.ItemConfiguracao
        fields = '__all__'

class faturamentoItemConteudo(serializers.ModelSerializer):
    class Meta:
        model = models.FaturamentoItemConteudo
        fields = '__all__'
