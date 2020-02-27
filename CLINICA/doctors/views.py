from django.views.generic import TemplateView
from .models import Doctor
from .forms import DoctorForm


class DoctorList(TemplateView):
    template_name = 'doctors/doctor_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctors'] = Doctor.objects.all()
        context['form'] = DoctorForm(self.request.POST or None)
        return context
