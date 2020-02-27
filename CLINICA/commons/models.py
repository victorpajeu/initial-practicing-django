from django.db import models


class Person(models.Model):
    name = models.CharField("Nome", max_length=100)
    age = models.IntegerField("Idade")
    cpf = models.IntegerField("CPF")

    class Meta:
        abstract = True
