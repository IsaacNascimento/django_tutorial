# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AtributoCredencial(models.Model):
    id = models.UUIDField(primary_key=True)
    ds_credencial = models.CharField(max_length=100)
    js_atributo = models.JSONField()
    dt_sincronizacao = models.DateTimeField()
    contrato = models.ForeignKey('Contrato', models.DO_NOTHING)
    ds_observacao = models.CharField(max_length=250, blank=True, null=True)
    dt_alteracao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'atributo_credencial'


class AtributoGenerico(models.Model):
    id = models.IntegerField(primary_key=True)
    tabela_id = models.IntegerField()
    no_tabela = models.CharField(max_length=255)
    no_atributo = models.CharField(max_length=255)
    no_substituir = models.CharField(max_length=255, blank=True, null=True)
    ds_titulo = models.CharField(max_length=255, blank=True, null=True)
    bo_obrigatorio = models.BooleanField()
    dt_sincronizacao = models.DateTimeField()
    contrato = models.ForeignKey('Contrato', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'atributo_generico'


class Camada(models.Model):
    id = models.IntegerField(primary_key=True)
    no_camada = models.CharField(max_length=100)
    bo_ativo = models.BooleanField()
    dt_sincronizacao = models.DateTimeField()
    contrato = models.ForeignKey('Contrato', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'camada'


class Classe(models.Model):
    id = models.IntegerField(primary_key=True)
    no_classe = models.CharField(max_length=100)
    no_descricao = models.CharField(max_length=100)
    ds_tag = models.CharField(max_length=100)
    bo_manual = models.BooleanField()
    bo_ativo = models.BooleanField()
    dt_sincronizacao = models.DateTimeField()
    contrato = models.ForeignKey('Contrato', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'classe'


class ClasseProvedor(models.Model):
    id = models.IntegerField(primary_key=True)
    dt_sincronizacao = models.DateTimeField()
    classe = models.ForeignKey(Classe, models.DO_NOTHING)
    provedor = models.ForeignKey('Provedor', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'classe_provedor'


class Contrato(models.Model):
    id = models.IntegerField(primary_key=True)
    no_entidade = models.CharField(max_length=150)
    no_contrato = models.CharField(max_length=150)
    vl_unidade_servico = models.DecimalField(max_digits=12, decimal_places=2)
    nu_dia_faturamento = models.CharField(max_length=2)
    bo_ativo = models.BooleanField()
    dt_sincronizacao = models.DateTimeField()
    tp_regra_cobranca = models.CharField(max_length=14)
    tp_relevancia = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'contrato'


class ContratoAcessoInventarioExterno(models.Model):
    st_ferramenta = models.CharField(max_length=4)
    ds_url_ip = models.TextField()
    nu_porta = models.TextField()
    no_banco = models.TextField()
    no_usuario = models.TextField()
    ds_senha = models.TextField()
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    dt_cadastro = models.DateTimeField()
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'contrato_acesso_inventario_externo'


class ContratoAcessoItsm(models.Model):
    st_itsm = models.CharField(max_length=30)
    st_conector = models.CharField(max_length=30)
    ds_url_ip = models.TextField()
    nu_porta = models.TextField()
    no_banco = models.TextField()
    no_usuario = models.TextField()
    ds_senha = models.TextField()
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    dt_cadastro = models.DateTimeField()
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'contrato_acesso_itsm'


class ContratoIntegracaoItsm(models.Model):
    js_configuracao = models.JSONField(blank=True, null=True)
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    dt_cadastro = models.DateTimeField()
    item_configuracao = models.ForeignKey('ItemConfiguracao', models.DO_NOTHING)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'contrato_integracao_itsm'


class Diversidade(models.Model):
    id = models.IntegerField(primary_key=True)
    nu_diversidade = models.IntegerField()
    vl_percentual = models.DecimalField(max_digits=12, decimal_places=2)
    ds_diversidade = models.CharField(max_length=80, blank=True, null=True)
    dt_sincronizacao = models.DateTimeField()
    contrato = models.ForeignKey(Contrato, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'diversidade'


class Evento(models.Model):
    no_app_executor = models.CharField(max_length=20)
    st_tipo = models.CharField(max_length=255)
    js_entrada = models.JSONField(blank=True, null=True)
    js_retorno = models.JSONField(blank=True, null=True)
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    dt_cadastro = models.DateTimeField()
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)
    st_situacao = models.CharField(max_length=15)
    bo_lido = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'evento'


class Faturamento(models.Model):
    qt_contabilizado = models.IntegerField()
    qt_nao_contabilizado = models.IntegerField(blank=True, null=True)
    vl_total_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    vl_total_grupo = models.DecimalField(max_digits=12, decimal_places=2)
    vl_total_mensal = models.DecimalField(max_digits=12, decimal_places=2)
    dt_mes_referencia = models.DateField()
    st_situacao = models.CharField(max_length=9)
    dt_faturado = models.DateTimeField(blank=True, null=True)
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    dt_cadastro = models.DateTimeField()
    contrato = models.ForeignKey(Contrato, models.DO_NOTHING)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)
    bo_regra_cobranca = models.BooleanField()
    bo_diario = models.BooleanField()
    dt_final_simulacao = models.DateTimeField(blank=True, null=True)
    dt_inicial_simulacao = models.DateTimeField(blank=True, null=True)
    vl_unidade_servico = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    qt_relevancia_sem_validacao = models.IntegerField(blank=True, null=True)
    bo_faturado = models.BooleanField()
    ds_observacao = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faturamento'


class FaturamentoComparativoRastreabilidade(models.Model):
    dt_cadastro = models.DateTimeField()
    faturamento_dois = models.ForeignKey(Faturamento, models.DO_NOTHING, related_name='faturamento_dois_type')
    faturamento_um = models.ForeignKey(Faturamento, models.DO_NOTHING)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)
    bo_cancelado = models.BooleanField()
    ds_observacao = models.CharField(max_length=255, blank=True, null=True)
    bo_faturado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'faturamento_comparativo_rastreabilidade'


class FaturamentoItem(models.Model):
    qt_contabilizado = models.IntegerField()
    qt_nao_contabilizado = models.IntegerField(blank=True, null=True)
    nu_diversidade = models.IntegerField()
    vl_diversidade = models.DecimalField(max_digits=12, decimal_places=2)
    nu_relevancia = models.IntegerField(blank=True, null=True)
    vl_relevancia = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    vl_item = models.DecimalField(max_digits=12, decimal_places=2)
    vl_total_item = models.DecimalField(max_digits=12, decimal_places=2)
    vl_total_faturado = models.DecimalField(max_digits=12, decimal_places=2)
    dt_cadastro = models.DateTimeField()
    faturamento = models.ForeignKey(Faturamento, models.DO_NOTHING)
    item_configuracao = models.ForeignKey('ItemConfiguracao', models.DO_NOTHING)
    js_relevancia = models.JSONField(blank=True, null=True)
    qt_relevancia_sem_validacao = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faturamento_item'


class FaturamentoItemConteudo(models.Model):
    js_contabilizado = models.JSONField()
    js_nao_contabilizado = models.JSONField(blank=True, null=True)
    js_condicional = models.JSONField(blank=True, null=True)
    js_diversidade = models.JSONField(blank=True, null=True)
    dt_cadastro = models.DateTimeField()
    faturamento_item = models.ForeignKey(FaturamentoItem, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'faturamento_item_conteudo'


class GerenciaConfiguracao(models.Model):
    ds_tag = models.CharField(max_length=100)
    hub_hash = models.CharField(max_length=150)
    js_data = models.JSONField(blank=True, null=True)
    ds_justificativa = models.CharField(max_length=255, blank=True, null=True)
    bo_ativo = models.BooleanField()
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    dt_cadastro = models.DateTimeField()
    contrato = models.ForeignKey(Contrato, models.DO_NOTHING)
    gerencia_configuracao_situacao = models.ForeignKey('GerenciaConfiguracaoSituacao', models.DO_NOTHING)
    item_configuracao = models.ForeignKey('ItemConfiguracao', models.DO_NOTHING)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gerencia_configuracao'


class GerenciaConfiguracaoSituacao(models.Model):
    no_situacao = models.CharField(max_length=150)
    ds_observacao = models.CharField(max_length=250)
    bo_ativo = models.BooleanField()
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    dt_cadastro = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'gerencia_configuracao_situacao'


class ItemConfiguracao(models.Model):
    id = models.IntegerField(primary_key=True)
    no_item = models.CharField(max_length=150)
    vl_item = models.DecimalField(max_digits=12, decimal_places=2)
    nu_dia_regra_cobranca = models.IntegerField(blank=True, null=True)
    bo_ativo = models.BooleanField()
    dt_sincronizacao = models.DateTimeField()
    camada = models.ForeignKey(Camada, models.DO_NOTHING)
    classe = models.ForeignKey(Classe, models.DO_NOTHING)
    contrato = models.ForeignKey(Contrato, models.DO_NOTHING)
    relevancia = models.ForeignKey('Relevancia', models.DO_NOTHING, blank=True, null=True)
    bo_rastreabilidade = models.BooleanField()
    tp_regra_cobranca = models.CharField(max_length=14)
    bo_hibrido = models.BooleanField()
    dt_hibrido = models.DateField(blank=True, null=True)
    tp_relevancia = models.CharField(max_length=10)
    responsavel = models.ForeignKey('ItemConfiguracaoResponsavel', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_configuracao'


class ItemConfiguracaoCondicional(models.Model):
    bo_aplica_regra = models.BooleanField()
    ds_justificativa = models.CharField(max_length=255)
    dt_duracao = models.DateField(blank=True, null=True)
    dt_cadastro = models.DateTimeField()
    item_configuracao = models.ForeignKey(ItemConfiguracao, models.DO_NOTHING)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)
    dt_inicio_duracao = models.DateField(blank=True, null=True)
    js_condicao = models.JSONField()
    no_condicional = models.TextField()

    class Meta:
        managed = False
        db_table = 'item_configuracao_condicional'


class ItemConfiguracaoDiversidade(models.Model):
    no_grupo = models.CharField(max_length=150)
    no_atributo = models.CharField(max_length=255)
    js_item = models.JSONField()
    dt_cadastro = models.DateTimeField()
    item_configuracao = models.ForeignKey(ItemConfiguracao, models.DO_NOTHING)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_configuracao_diversidade'


class ItemConfiguracaoManual(models.Model):
    js_manual = models.JSONField()
    dt_cadastro = models.DateTimeField()
    item_configuracao = models.ForeignKey(ItemConfiguracao, models.DO_NOTHING)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)
    bo_ativo = models.BooleanField()
    dt_fim_duracao = models.DateField(blank=True, null=True)
    dt_desativacao = models.DateField(blank=True, null=True)
    no_usuario_desativacao = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_configuracao_manual'


class ItemConfiguracaoRastreabilidade(models.Model):
    js_item = models.JSONField()
    nu_chamado = models.CharField(max_length=150, blank=True, null=True)
    bo_validado = models.BooleanField()
    st_tipo = models.CharField(max_length=8)
    dt_validacao = models.DateField(blank=True, null=True)
    dt_rastreabilidade = models.DateField()
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    dt_cadastro = models.DateTimeField()
    item_configuracao = models.ForeignKey(ItemConfiguracao, models.DO_NOTHING)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)
    dt_mes_referencia = models.DateField(blank=True, null=True)
    faturamento_comparativo_rastreabilidade = models.ForeignKey(FaturamentoComparativoRastreabilidade, models.DO_NOTHING, blank=True, null=True)
    dt_ticket = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_configuracao_rastreabilidade'


class ItemConfiguracaoRelatorio(models.Model):
    js_data = models.JSONField(blank=True, null=True)
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    dt_cadastro = models.DateTimeField()
    item_configuracao = models.OneToOneField(ItemConfiguracao, models.DO_NOTHING)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_configuracao_relatorio'


class ItemConfiguracaoRelevancia(models.Model):
    dt_cadastro = models.DateTimeField()
    item_configuracao = models.ForeignKey(ItemConfiguracao, models.DO_NOTHING)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)
    js_data = models.JSONField(blank=True, null=True)
    nu_relevancia = models.IntegerField(blank=True, null=True)
    bo_ativo = models.BooleanField()
    bo_validado = models.BooleanField()
    ds_justificativa = models.CharField(max_length=255, blank=True, null=True)
    ds_relevancia = models.CharField(max_length=80)
    ds_tag = models.CharField(max_length=100)
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    dt_validacao = models.DateField(blank=True, null=True)
    hub_hash = models.CharField(max_length=150)
    vl_percentual = models.DecimalField(max_digits=12, decimal_places=2)
    dt_mes_referencia = models.DateField(blank=True, null=True)
    bo_planejado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'item_configuracao_relevancia'


class ItemConfiguracaoResponsavel(models.Model):
    no_responsavel = models.CharField(max_length=150)
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    dt_cadastro = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'item_configuracao_responsavel'


class MonitoramentoAcompanhamento(models.Model):
    ds_comparativo = models.TextField()
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    dt_cadastro = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'monitoramento_acompanhamento'


class MonitoramentoBaseReferencia(models.Model):
    bo_ativo = models.BooleanField()
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    dt_cadastro = models.DateTimeField()
    faturamento = models.ForeignKey(Faturamento, models.DO_NOTHING)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monitoramento_base_referencia'


class MonitoramentoConfiguracao(models.Model):
    nu_porcentagem = models.IntegerField()
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    dt_cadastro = models.DateTimeField()
    item_configuracao = models.ForeignKey(ItemConfiguracao, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'monitoramento_configuracao'


class MonitoramentoItemConfiguracao(models.Model):
    ds_tag = models.CharField(max_length=100)
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    dt_cadastro = models.DateTimeField()
    item_configuracao = models.ForeignKey(ItemConfiguracao, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'monitoramento_item_configuracao'


class MonitoramentoItemConfiguracaoConteudo(models.Model):
    dt_inventario_a = models.DateTimeField()
    qt_inventario_a = models.IntegerField()
    dt_inventario_b = models.DateTimeField()
    qt_inventario_b = models.IntegerField()
    qt_inventario_diferenca_a_b = models.IntegerField()
    co_faturamento_a = models.IntegerField()
    ds_faturamento_a = models.CharField(max_length=255)
    qt_faturamento_a = models.IntegerField()
    co_faturamento_b = models.IntegerField()
    ds_faturamento_b = models.CharField(max_length=255)
    qt_faturamento_b = models.IntegerField()
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    dt_cadastro = models.DateTimeField()
    monitoramento_item_configuracao = models.ForeignKey(MonitoramentoItemConfiguracao, models.DO_NOTHING)
    qt_faturamento_diferenca_exclusao = models.IntegerField(blank=True, null=True)
    qt_faturamento_diferenca_inclusao = models.IntegerField(blank=True, null=True)
    st_situacao = models.CharField(max_length=255, blank=True, null=True)
    nu_porcentagem = models.IntegerField(blank=True, null=True)
    bo_alerta = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'monitoramento_item_configuracao_conteudo'


class MonitoramentoItemConfiguracaoNotas(models.Model):
    ds_observacao = models.CharField(max_length=255, blank=True, null=True)
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    dt_cadastro = models.DateTimeField()
    monitoramento_item_configuracao = models.ForeignKey(MonitoramentoItemConfiguracao, models.DO_NOTHING)
    monitoramento_situacao = models.ForeignKey('MonitoramentoSituacao', models.DO_NOTHING)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monitoramento_item_configuracao_notas'


class MonitoramentoSituacao(models.Model):
    no_situacao = models.CharField(max_length=150)
    bo_ativo = models.BooleanField()
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    dt_cadastro = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'monitoramento_situacao'


class Provedor(models.Model):
    id = models.IntegerField(primary_key=True)
    no_provedor = models.CharField(max_length=100)
    ds_provedor = models.CharField(max_length=150, blank=True, null=True)
    no_modulo = models.CharField(max_length=200)
    no_atributo_retorno = models.CharField(max_length=100)
    st_tipo = models.CharField(max_length=10, blank=True, null=True)
    bo_ativo = models.BooleanField()
    dt_sincronizacao = models.DateTimeField()
    atributo_credencial = models.ForeignKey(AtributoCredencial, models.DO_NOTHING, blank=True, null=True)
    contrato = models.ForeignKey(Contrato, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'provedor'


class Relevancia(models.Model):
    id = models.IntegerField(primary_key=True)
    nu_relevancia = models.IntegerField()
    vl_percentual = models.DecimalField(max_digits=12, decimal_places=2)
    ds_relevancia = models.CharField(max_length=80, blank=True, null=True)
    dt_sincronizacao = models.DateTimeField()
    contrato = models.ForeignKey(Contrato, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'relevancia'


class Usuario(models.Model):
    no_usuario = models.CharField(max_length=150)
    ds_email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_admin = models.BooleanField()
    is_active = models.BooleanField()
    jwt_secret = models.UUIDField()
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    dt_cadastro = models.DateTimeField()
    grupo = models.ForeignKey('UsuarioGrupo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'usuario'


class UsuarioGrupo(models.Model):
    id = models.IntegerField(primary_key=True)
    no_grupo = models.CharField(max_length=100)
    ds_tag = models.CharField(max_length=50)
    bo_tem_regra = models.BooleanField()
    st_ambiente = models.CharField(max_length=7)
    bo_ativo = models.BooleanField()
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    dt_cadastro = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'usuario_grupo'
