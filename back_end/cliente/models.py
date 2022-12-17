from django.db import models


class Cliente(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    rua = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField(db_column='CEP', max_length=8, blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(max_length=2, blank=True, null=True)
    cpf = models.CharField(db_column='CPF', max_length=11, blank=True, null=True)  # Field name made lowercase.
    cnpj = models.CharField(db_column='CNPJ', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'cliente'