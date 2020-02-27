from django.db import models


class Doctor(models.Model):
    name = models.CharField('Nome', max_length=100)
    age = models.IntegerField('Idade', null=False)
    crm = models.IntegerField('CRM', null=False)
    create_at = models.DateTimeField('Data e tempo de Criação', auto_now_add=True)
    update_at = models.DateTimeField('Data e tempo de alteração', auto_now=True)

    def __str__(self):
        return self.name
