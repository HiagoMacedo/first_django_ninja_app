from django.db import models



class Cidade(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    populacao = models.IntegerField(blank=True, null=True)
    anofundacao = models.IntegerField(db_column='anoFundacao', blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        db_table = 'cidade'