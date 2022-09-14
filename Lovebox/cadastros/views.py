from django.views.generic import TemplateView
from .models import Medicamento, ProfissionalSaude, DosesTratamento, Cuidador, Paciente, Tratamento
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from braces.views import GroupRequiredMixin

# Create your views here.
class IndexView(TemplateView):
    template_name = "cadastros/index.html"

class PaginaInicialView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['ultimos_medicamentos'] = Medicamento.objects.all().reverse()[0:10]
        return context

class MedicamentoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Medicamento
    fields = ['nome_comercial', 'laboratorio', 'principio_ativo', 'dose_diaria_maxima', 'forma_farmaceutica', 'concentracao', 'via_administracao', 'grupo_etario', 'tarja']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-medicamentos')

class ProfissionalSaudeCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = ProfissionalSaude
    fields = ['nome', 'telefone', 'endereco', 'consultorio', 'email', 'redes_sociais', 'crc']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-profissionais-saude')

class DosesTratamentoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = DosesTratamento
    fields = ['alarme', 'compartimento_caixa', 'tempo_alerta_especifico', 'status_tratamento']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-doses-tratamentos')

    def form_valid(self, form):
        #define o usuario como usuário logado
        form.instance.usuario = self.request.user

        #valida os dados do form antes de criar o objeto (não está no banco)
        url = super().form_valid(form)

        #nesse ponto, o objeto já foi inserido no banco de dados
        print(self.object.usuario)
        
        return url


class CuidadorCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Cuidador
    fields = ['nome', 'telefone', 'crc', 'redes_sociais']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-cuidadores')

    def form_valid(self, form):
        form.instance.usuario = self.request.user

        #valida os dados do form antes de criar o objeto (não está no banco)
        url = super().form_valid(form)

        #nesse ponto, o objeto já foi inserido no banco de dados
        print(self.object.usuario)
        
        return url


class PacienteCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Paciente
    fields = ['nome', 'telefone', 'data_nascimento', 'documento', 'cep', 'logradouro', 'numero', 'bairro', 'anamnese', 'redes_sociais', 'cuidador']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-pacientes')

    def form_valid(self, form):
        form.instance.usuario = self.request.user

        #valida os dados do form antes de criar o objeto (não está no banco)
        url = super().form_valid(form)

        #nesse ponto, o objeto já foi inserido no banco de dados
        print(self.object.usuario)
        
        return url

class TratamentoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Tratamento
    fields = ['prescrito_por', 'data_prescricao', 'medicamento', 'frequencia_diaria', 'dose', 'unidade_medida', 'data_inicio', 'tipo_tratamento', 'periodo_tratamento', 'data_fim', 'observacao', 'lote', 'validade', 'embalagem_fracionavel', 'quantidade_total_embalagem', 'amostra_gratis', 'status_tratamento', 'paciente']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-tratamentos')

    def form_valid(self, form):
        form.instance.usuario = self.request.user

        #valida os dados do form antes de criar o objeto (não está no banco)
        url = super().form_valid(form)

        #nesse ponto, o objeto já foi inserido no banco de dados
        print(self.object.usuario)
        
        return url

##### UPDATE#########
class MedicamentoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Medicamento
    fields = ['nome_comercial', 'laboratorio', 'principio_ativo', 'dose_diaria_maxima', 'forma_farmaceutica', 'concentracao', 'via_administracao', 'grupo_etario', 'tarja']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-medicamentos')

class ProfissionalSaudeUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = ProfissionalSaude
    fields = ['nome', 'telefone', 'endereco', 'consultorio', 'email', 'redes_sociais', 'crc']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-profissionais-saude')

    

class DosesTratamentoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = DosesTratamento
    fields = ['alarme', 'compartimento_caixa', 'tempo_alerta_especifico', 'status_tratamento']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-doses-tratamentos')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(DosesTratamento, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

class CuidadorUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Cuidador
    fields = ['nome', 'telefone', 'crc', 'redes_sociais']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-cuidadores')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Cuidador, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

class PacienteUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Paciente
    fields = ['nome', 'telefone', 'data_nascimento', 'documento', 'cep', 'logradouro', 'numero', 'bairro', 'anamnese', 'redes_sociais', 'cuidador']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-pacientes')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Paciente, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

class TratamentoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Tratamento
    fields = ['prescrito_por', 'data_prescricao', 'medicamento', 'frequencia_diaria', 'dose', 'unidade_medida', 'data_inicio', 'tipo_tratamento', 'periodo_tratamento', 'data_fim', 'observacao', 'lote', 'validade', 'embalagem_fracionavel', 'quantidade_total_embalagem', 'status_tratamento', 'paciente']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-tratamentos')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Tratamento, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

##### DELETE #########
class MedicamentoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Medicamento
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-medicamentos')

    def get_object(self):
        self.object = get_object_or_404(
            Medicamento, usuario=self.request.user, pk=self.kwargs['pk'])
        return self.object

class ProfissionalSaudeDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = ProfissionalSaude
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-profissionais-saude')

class DosesTratamentoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = DosesTratamento
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-doses-tratamentos')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(DosesTratamento, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

class CuidadorDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Cuidador
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cuidadores')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Cuidador, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

class PacienteDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Paciente
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-pacientes')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Paciente, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

class TratamentoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Tratamento
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-tratamentos')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Tratamento, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


##### LIST #########
class MedicamentoList(ListView):
    model = Medicamento
    template_name = 'cadastros/listar-medicamentos.html'

class ProfissionalSaudeList(ListView):
    model = ProfissionalSaude
    template_name = 'cadastros/listar-profissionais-saude.html'

class DosesTratamentoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = DosesTratamento
    template_name = 'cadastros/listar-doses-tratamentos.html'

    def get_queryset(self):
        self.object_list = DosesTratamento.objects.filter(usuario=self.request.user)
        return self.object_list

class CuidadorList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Cuidador
    template_name = 'cadastros/listar-cuidadores.html'

    def get_queryset(self):
        self.object_list = Cuidador.objects.filter(usuario=self.request.user)
        return self.object_list

class PacienteList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Paciente
    template_name = 'cadastros/listar-pacientes.html'

    def get_queryset(self):
        self.object_list = Paciente.objects.filter(usuario=self.request.user)
        return self.object_list

class TratamentoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Tratamento
    template_name = 'cadastros/listar-tratamentos.html'

    def get_queryset(self):
        self.object_list = Tratamento.objects.filter(usuario=self.request.user)
        return self.object_list


