from django.db import models



class Telefone(models.Model):
    codigocliente = models.IntegerField(db_column='codigoCliente', primary_key=True)  # Field name made lowercase.
    numero = models.CharField(max_length=11)

    class Meta:
        db_table = 'telefone'
        unique_together = (('codigocliente', 'numero'),)