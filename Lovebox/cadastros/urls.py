from django.urls import path
from .views import IndexView, MedicamentoCreate, ProfissionalSaudeCreate, DosesTratamentoCreate, CuidadorCreate, PacienteCreate, TratamentoCreate, MedicamentoUpdate, ProfissionalSaudeUpdate, DosesTratamentoUpdate, CuidadorUpdate, PacienteUpdate, TratamentoUpdate, MedicamentoDelete, ProfissionalSaudeDelete, DosesTratamentoDelete, CuidadorDelete, PacienteDelete, TratamentoDelete, MedicamentoList, ProfissionalSaudeList, DosesTratamentoList, CuidadorList, PacienteList, TratamentoList

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('cadastrar/medicamento/', MedicamentoCreate.as_view(), name='cadastrar-medicamento'),
    path('cadastrar/profissional_saude/', ProfissionalSaudeCreate.as_view(), name='cadastrar-profissional-saude'),
    path('cadastrar/doses_tratamento/', DosesTratamentoCreate.as_view(), name='cadastrar-doses-tratamento'),
    path('cadastrar/cuidador/', CuidadorCreate.as_view(), name='cadastrar-cuidador'),
    path('cadastrar/paciente/', PacienteCreate.as_view(), name='cadastrar-paciente'),
    path('cadastrar/tratamento/', TratamentoCreate.as_view(), name='cadastrar-tratamento'),

    ####UPDATE####
    path('atualizar/medicamento/<int:pk>/', MedicamentoUpdate.as_view(), name='atualizar-medicamento'),
    path('atualizar/profissional_saude/<int:pk>/', ProfissionalSaudeUpdate.as_view(), name='atualizar-profissional-saude'),
    path('atualizar/doses_tratamento/<int:pk>/', DosesTratamentoUpdate.as_view(), name='atualizar-doses-tratamento'),
    path('atualizar/cuidador/<int:pk>/', CuidadorUpdate.as_view(), name='atualizar-cuidador'),
    path('atualizar/paciente/<int:pk>/', PacienteUpdate.as_view(), name='atualizar-paciente'),
    path('atualizar/tratamento/<int:pk>/', TratamentoUpdate.as_view(), name='atualizar-tratamento'),

    ####DELETE####
    path('excluir/medicamento/<int:pk>/', MedicamentoDelete.as_view(), name='excluir-medicamento'),
    path('excluir/profissional_saude/<int:pk>/', ProfissionalSaudeDelete.as_view(), name='excluir-profissional-saude'),
    path('excluir/doses_tratamento/<int:pk>/', DosesTratamentoDelete.as_view(), name='excluir-doses-tratamento'),
    path('excluir/cuidador/<int:pk>/', CuidadorDelete.as_view(), name='excluir-cuidador'),
    path('excluir/paciente/<int:pk>/', PacienteDelete.as_view(), name='excluir-paciente'),
    path('excluir/tratamento/<int:pk>/', TratamentoDelete.as_view(), name='excluir-tratamento'),

    ####LIST####
    path('listar/medicamentos/', MedicamentoList.as_view(), name='listar-medicamentos'),
    path('listar/profissionais_saude/', ProfissionalSaudeList.as_view(), name='listar-profissionais-saude'),
    path('listar/doses_tratamentos/', DosesTratamentoList.as_view(), name='listar-doses-tratamentos'),
    path('listar/cuidadores/', CuidadorList.as_view(), name='listar-cuidadores'),
    path('listar/pacientes/', PacienteList.as_view(), name='listar-pacientes'),
    path('listar/tratamentos/', TratamentoList.as_view(), name='listar-tratamentos'),
]