from django.db import models



class Filial(models.Model):
    codigo = models.IntegerField(primary_key=True)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    rua = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField(db_column='CEP', max_length=8, blank=True, null=True)  # Field name made lowercase.
    idcidade = models.ForeignKey('cidade.Cidade', models.DO_NOTHING, db_column='idCidade', blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        db_table = 'filial'