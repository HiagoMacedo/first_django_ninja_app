# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models











class Filial(models.Model):
    codigo = models.IntegerField(primary_key=True)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    rua = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField(db_column='CEP', max_length=8, blank=True, null=True)  # Field name made lowercase.
    idcidade = models.ForeignKey(Cidade, models.DO_NOTHING, db_column='idCidade', blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        db_table = 'filial'


class Telefone(models.Model):
    codigocliente = models.IntegerField(db_column='codigoCliente', primary_key=True)  # Field name made lowercase.
    numero = models.CharField(max_length=11)

    class Meta:
        db_table = 'telefone'
        unique_together = (('codigocliente', 'numero'),)


class Veiculo(models.Model):
    placa = models.CharField(max_length=7, blank=True, null=True)
    modelo = models.CharField(max_length=20, blank=True, null=True)
    numportas = models.IntegerField(db_column='numPortas', blank=True, null=True)  # Field name made lowercase.
    arcondicionado = models.CharField(db_column='arCondicionado', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vencimentoseguro = models.DateField(db_column='vencimentoSeguro', blank=True, null=True)  # Field name made lowercase.
    codfilial = models.ForeignKey(Filial, models.DO_NOTHING, db_column='codFilial', blank=True, null=True)  # Field name made lowercase.
    marca = models.CharField(max_length=20, blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    valordiaria = models.DecimalField(db_column='valorDiaria', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'veiculo'
