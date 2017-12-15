from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.TextField()
    cpf = models.TextField()
    login = models.TextField()
    chave = models.TextField()
    data_cadastro = models.BigIntegerField()

    def __str__(self):
        return self.nome

class Corretora(models.Model):
    descricao = models.TextField()
    fantasia = models.TextField()
    cnpj = models.TextField()
    banco_codigo = models.TextField()
    banco_agencia = models.TextField()
    banco_conta = models.TextField()
    banco_tipo = models.TextField()
    data_cadastro = models.BigIntegerField()

    def __str__(self):
        return self.descricao

class Operacao(models.Model):
    descricao = models.TextField()
    percentual_bmf = models.FloatField()
    percentual_ir = models.FloatField()

    def __str__(self):
        return self.descricao

class Lancamento(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    id_corretora = models.ForeignKey(Corretora, on_delete=models.DO_NOTHING)
    id_operacao = models.ForeignKey(Operacao, on_delete=models.DO_NOTHING)
    data_lancamento = models.BigIntegerField()
    data_pregao = models.BigIntegerField()
    numero_nota = models.BigIntegerField()
    valor_negocio = models.FloatField()
    valor_taxa_operacional = models.FloatField()
    valor_taxa_registro_bmf = models.FloatField()
    valor_taxa_emolumento_bmf = models.FloatField()
    valor_iss = models.FloatField()



