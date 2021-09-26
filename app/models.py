from django_cpf_cnpj.fields import CPFField, CNPJField
from django.db import models
from django.db.models import Model
from django.db.models import EmailField, DecimalField

class Empresa(models.Model):
    empresa = models.CharField(max_length=150)
    cnpj = CNPJField(masked=True)
    email = models.EmailField (max_length=50,  default="", )


class Produto(models.Model):
    produto = models.CharField(max_length=150)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=5, default="")
    descricao = models.CharField(max_length=150, default="")
    marca = models.CharField(max_length=50, default="")
    valor = models.DecimalField(max_digits=5, decimal_places=2, default="")