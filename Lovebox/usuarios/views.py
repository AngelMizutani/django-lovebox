from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

class UsuarioCreate(CreateView):
    template_name = "cadastros/formulario.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name='Usuarios')
        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        return url


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registrar"

        return context

