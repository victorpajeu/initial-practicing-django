from django.db import models
from commons.models import Person


class Doctor(Person):
    crm = models.IntegerField('CRM', null=False)
    create_at = models.DateTimeField('Data e tempo de Criação', auto_now_add=True)
    update_at = models.DateTimeField('Data e tempo de alteração', auto_now=True)

    def __str__(self):
        return self.name
