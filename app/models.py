from django.db import models

class Empresa(models.Model):
    empresa = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=150)


class Produto(models.Model):
    produto = models.CharField(max_length=150)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

