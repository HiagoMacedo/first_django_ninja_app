from django.db import models



class Contrato(models.Model):
    numero = models.IntegerField(unique=True, blank=True, null=True)
    idveiculo = models.OneToOneField('veiculo.Veiculo', models.DO_NOTHING, db_column='idVeiculo', primary_key=True)  # Field name made lowercase.
    codigocliente = models.ForeignKey('cliente.Cliente', models.DO_NOTHING, db_column='codigoCliente')  # Field name made lowercase.
    datasaida = models.DateField(db_column='dataSaida')  # Field name made lowercase.
    dataretorno = models.DateField(db_column='dataRetorno', blank=True, null=True)  # Field name made lowercase.
    datadevolucao = models.DateField(db_column='dataDevolucao', blank=True, null=True)  # Field name made lowercase.
    valorreserva = models.DecimalField(db_column='valorReserva', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    multa = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    valorpago = models.DecimalField(db_column='valorPago', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'contrato'
        unique_together = (('idveiculo', 'codigocliente', 'datasaida'),)
    