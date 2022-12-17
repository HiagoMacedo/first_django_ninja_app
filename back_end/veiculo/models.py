from django.db import models



class Veiculo(models.Model):
    placa = models.CharField(max_length=7, blank=True, null=True)
    modelo = models.CharField(max_length=20, blank=True, null=True)
    numportas = models.IntegerField(db_column='numPortas', blank=True, null=True)  # Field name made lowercase.
    arcondicionado = models.CharField(db_column='arCondicionado', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vencimentoseguro = models.DateField(db_column='vencimentoSeguro', blank=True, null=True)  # Field name made lowercase.
    codfilial = models.ForeignKey('filial.Filial', models.DO_NOTHING, db_column='codFilial', blank=True, null=True)  # Field name made lowercase.
    marca = models.CharField(max_length=20, blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    valordiaria = models.DecimalField(db_column='valorDiaria', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'veiculo'