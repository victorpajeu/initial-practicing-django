from django.forms import ModelForm
from .models import Doctor


class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'age', 'cpf', 'crm']