# from django.shortcuts import render
from django.views.generic import TemplateView
from Lovebox.cadastros.models import Medicamento
from braces.views import GroupRequiredMixin
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class MedicamentoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Medicamento
    template_name = 'cadastros/listar-medicamentos.html'
