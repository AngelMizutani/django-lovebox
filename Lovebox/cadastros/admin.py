from django.contrib import admin
from .models import Medicamento, ProfissionalSaude, DosesTratamento, Cuidador, Paciente, Tratamento

# Register your models here.
admin.site.register(Medicamento)
admin.site.register(ProfissionalSaude)
admin.site.register(DosesTratamento)
admin.site.register(Cuidador)
admin.site.register(Paciente)
admin.site.register(Tratamento)
