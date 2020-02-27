from django.db import models


class Person(models.Model):
    name = models.CharField("Nome", max_length=100)
    age = models.IntegerField("Idade", max_length=50)
    cpf = models.IntegerField("CPF", max_length=11)
