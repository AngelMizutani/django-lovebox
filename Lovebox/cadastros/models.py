from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Perfil(models.Model):
#     nome_completo = models.CharField(max_length=100)
#     cpf = models.CharField(max_length=14)
#     telefone = models.CharField(max_length=15)
#     usuario = models.OneToOneField(User, on_delete=models.PROTECT)

class Medicamento(models.Model):
    nome_comercial = models.CharField(max_length=100)
    laboratorio = models.CharField(max_length=50, verbose_name='Laboratório')
    principio_ativo = models.CharField(max_length=255, verbose_name='Princípio Ativo')
    dose_diaria_maxima = models.IntegerField(verbose_name='Dose Diária Máxima')
    forma_farmaceutica = models.CharField(max_length=50, verbose_name='Forma Farmacêutica')
    concentracao = models.CharField(max_length=10, verbose_name='Concentração')
    via_administracao = models.CharField(max_length=50, verbose_name='Via de administração')
    grupo_etario = models.CharField(max_length=50, verbose_name='Grupo Etário')
    tarja = models.CharField(max_length=100)

    def __str__(self):
        return '{} - {}'.format(self.nome_comercial, self.concentracao)

class ProfissionalSaude(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=50)
    endereco = models.CharField(max_length=255, verbose_name='Endereço')
    consultorio = models.CharField(max_length=255, verbose_name='Consultório')
    email = models.EmailField()
    redes_sociais = models.CharField(max_length=255, null=True, blank=True)
    crc = models.CharField(max_length=50, verbose_name='Conselho Regional de Classe')

    def __str__(self):
        return '{} - {} - {}'.format(self.nome, self.telefone, self.crc)

class DosesTratamento(models.Model):
    STATUS_TRATAMENTO = [
        ('A', 'Ativo'),
        ('I', 'Inativo')
    ]
    alarme = models.DateTimeField()
    compartimento_caixa = models.CharField(max_length=10, verbose_name='Compartimento')
    tempo_alerta_especifico = models.CharField(max_length=20, verbose_name='Tempo de alerta')
    status_ingestao = models.BooleanField(verbose_name='Status da Ingestão', default=False)
    status_sincronizacao = models.BooleanField(verbose_name='Status da Sincronização', default=False)
    status_tratamento = models.CharField(max_length=50, choices=STATUS_TRATAMENTO, default='A')

    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return '{} - {}'.format(self.alarme, self.compartimento_caixa)

class Cuidador(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=50)
    crc = models.CharField(max_length=50, verbose_name='Conselho Regional de Classe', null=True, blank=True)
    redes_sociais = models.CharField(max_length=255, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return '{} - {}'.format(self.nome, self.telefone)

class Paciente(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    documento = models.CharField(max_length=50)
    cep = models.CharField(max_length=20)
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    anamnese = models.TextField()
    redes_sociais = models.CharField(max_length=255, null=True, blank=True)
    cuidador = models.ForeignKey(Cuidador, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return '{} - {}'.format(self.nome, self.telefone)

class Tratamento(models.Model):
    UNIDADE_MEDIDA = [
        ('gt', 'Gota'),
        ('ml', 'ml'),
        ('cpm', 'Comprimido'),
    ]

    TIPO_TRATAMENTO = [
        ('cont', 'Contínuo'),
        ('temp', 'Temporário')
    ]

    STATUS_TRATAMENTO = [
        ('A', 'Ativo'),
        ('I', 'Inativo')
    ]

    prescrito_por = models.ForeignKey(ProfissionalSaude, on_delete=models.PROTECT)
    data_prescricao = models.DateField(verbose_name='Data da Prescrição')
    medicamento = models.ForeignKey(Medicamento, on_delete=models.PROTECT)
    frequencia_diaria = models.IntegerField(verbose_name='Frequência Diária')
    horarios_diarios = models.CharField(max_length=255, verbose_name='Horários Diários')
    dose = models.DecimalField(max_digits=7, decimal_places=3)
    unidade_medida = models.CharField(max_length=100, verbose_name='Unidade de Medida', choices=UNIDADE_MEDIDA)
    data_inicio = models.DateTimeField(verbose_name='Data de início')
    tipo_tratamento = models.CharField(max_length=50, verbose_name='Tipo de Tratamento', choices=TIPO_TRATAMENTO)
    periodo_tratamento = models.IntegerField(verbose_name='Período de Tratamento')
    data_fim = models.DateTimeField(verbose_name='Data de Término do Tratamento')
    observacao = models.TextField(verbose_name='Observação')
    lote = models.CharField(max_length=50)
    validade = models.DateField()
    embalagem_fracionavel = models.BooleanField(verbose_name='Embalagem Fracionável?')
    quantidade_total_embalagem = models.IntegerField(verbose_name='Quantidade Total por Embalagem')
    amostra_gratis = models.BooleanField(verbose_name='Amostra Grátis')
    status_tratamento = models.CharField(max_length=50, choices=STATUS_TRATAMENTO)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return '{} - {} - {}'.format(self.paciente.nome, self.medicamento.nome_comercial, self.horarios_diarios)