from django.views.generic import TemplateView
from .models import Medicamento, ProfissionalSaude, DosesTratamento, Cuidador, Paciente, Tratamento
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class IndexView(TemplateView):
    template_name = "cadastros/index.html"

class MedicamentoCreate(LoginRequiredMixin, CreateView):
    model = Medicamento
    fields = ['nome_comercial', 'laboratorio', 'principio_ativo', 'dose_diaria_maxima', 'forma_farmaceutica', 'concentracao', 'via_administracao', 'grupo_etario', 'tarja']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-medicamentos')
    # login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.usuario = self.request.user

        #valida os dadois do form antes de criar o objeto (não está no banco)
        url = super().form_valid(form)

        #nesse ponto, o objeto já foi inserido no banco de dados
        print(self.object.usuario)
        
        return url


class ProfissionalSaudeCreate(LoginRequiredMixin, CreateView):
    model = ProfissionalSaude
    fields = ['nome', 'telefone', 'endereco', 'consultorio', 'email', 'redes_sociais', 'crc']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-profissionais-saude')


class DosesTratamentoCreate(LoginRequiredMixin, CreateView):
    model = DosesTratamento
    fields = ['alarme', 'compartimento_caixa', 'tempo_alerta_especifico', 'status_tratamento']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-doses-tratamentos')


class CuidadorCreate(LoginRequiredMixin, CreateView):
    model = Cuidador
    fields = ['nome', 'telefone', 'crc', 'redes_sociais']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-cuidadores')


class PacienteCreate(LoginRequiredMixin, CreateView):
    model = Paciente
    fields = ['nome', 'telefone', 'data_nascimento', 'documento', 'cep', 'logradouro', 'numero', 'bairro', 'anamnese', 'redes_sociais', 'cuidador']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-pacientes')


class TratamentoCreate(LoginRequiredMixin, CreateView):
    model = Tratamento
    fields = ['prescrito_por', 'data_prescricao', 'medicamento', 'frequencia_diaria', 'dose', 'unidade_medida', 'data_inicio', 'tipo_tratamento', 'periodo_tratamento', 'data_fim', 'observacao', 'lote', 'validade', 'embalagem_fracionavel', 'quantidade_total_embalagem', 'amostra_gratis', 'status_tratamento', 'paciente']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-tratamentos')

##### UPDATE#########
class MedicamentoUpdate(UpdateView):
    model = Medicamento
    fields = ['nome_comercial', 'laboratorio', 'principio_ativo', 'dose_diaria_maxima', 'forma_farmaceutica', 'concentracao', 'via_administracao', 'grupo_etario', 'tarja']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-medicamentos')

class ProfissionalSaudeUpdate(UpdateView):
    model = ProfissionalSaude
    fields = ['nome', 'telefone', 'endereco', 'consultorio', 'email', 'redes_sociais', 'crc']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-profissionais-saude')

class DosesTratamentoUpdate(UpdateView):
    model = DosesTratamento
    fields = ['alarme', 'compartimento_caixa', 'tempo_alerta_especifico', 'status_tratamento']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-doses-tratamentos')

class CuidadorUpdate(UpdateView):
    model = Cuidador
    fields = ['nome', 'telefone', 'crc', 'redes_sociais']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-cuidadores')

class PacienteUpdate(UpdateView):
    model = Paciente
    fields = ['nome', 'telefone', 'data_nascimento', 'documento', 'cep', 'logradouro', 'numero', 'bairro', 'anamnese', 'redes_sociais', 'cuidador']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-pacientes')

class TratamentoUpdate(UpdateView):
    model = Tratamento
    fields = ['prescrito_por', 'data_prescricao', 'medicamento', 'frequencia_diaria', 'dose', 'unidade_medida', 'data_inicio', 'tipo_tratamento', 'periodo_tratamento', 'data_fim', 'observacao', 'lote', 'validade', 'embalagem_fracionavel', 'quantidade_total_embalagem', 'status_tratamento', 'paciente']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-tratamentos')

##### DELETE #########
class MedicamentoDelete(DeleteView):
    model = Medicamento
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-medicamentos')

class ProfissionalSaudeDelete(DeleteView):
    model = ProfissionalSaude
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-profissionais-saude')

class DosesTratamentoDelete(DeleteView):
    model = DosesTratamento
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-doses-tratamentos')

class CuidadorDelete(DeleteView):
    model = Cuidador
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cuidadores')

class PacienteDelete(DeleteView):
    model = Paciente
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-pacientes')

class TratamentoDelete(DeleteView):
    model = Tratamento
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-tratamentos')


##### LIST #########
class MedicamentoList(ListView):
    model = Medicamento
    template_name = 'cadastros/listar-medicamentos.html'

class ProfissionalSaudeList(ListView):
    model = ProfissionalSaude
    template_name = 'cadastros/listar-profissionais-saude.html'

class DosesTratamentoList(ListView):
    model = DosesTratamento
    template_name = 'cadastros/listar-doses-tratamentos.html'

class CuidadorList(ListView):
    model = Cuidador
    template_name = 'cadastros/listar-cuidadores.html'

class PacienteList(ListView):
    model = Paciente
    template_name = 'cadastros/listar-pacientes.html'

class TratamentoList(ListView):
    model = Tratamento
    template_name = 'cadastros/listar-tratamentos.html'