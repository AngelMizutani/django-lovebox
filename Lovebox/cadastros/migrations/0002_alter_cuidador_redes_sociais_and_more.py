# Generated by Django 4.0.4 on 2022-05-29 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuidador',
            name='redes_sociais',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dosestratamento',
            name='status_ingestao',
            field=models.BooleanField(default=False, verbose_name='Status da Ingestão'),
        ),
        migrations.AlterField(
            model_name='dosestratamento',
            name='status_sincronizacao',
            field=models.BooleanField(default=False, verbose_name='Status da Sincronização'),
        ),
        migrations.AlterField(
            model_name='dosestratamento',
            name='status_tratamento',
            field=models.CharField(choices=[('A', 'Ativo'), ('I', 'Inativo')], default='A', max_length=50),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='redes_sociais',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profissionalsaude',
            name='redes_sociais',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tratamento',
            name='embalagem_fracionavel',
            field=models.BooleanField(verbose_name='Embalagem Fracionável?'),
        ),
        migrations.AlterField(
            model_name='tratamento',
            name='status_tratamento',
            field=models.CharField(choices=[('A', 'Ativo'), ('I', 'Inativo')], max_length=50),
        ),
        migrations.AlterField(
            model_name='tratamento',
            name='tipo_tratamento',
            field=models.CharField(choices=[('cont', 'Contínuo'), ('temp', 'Temporário')], max_length=50, verbose_name='Tipo de Tratamento'),
        ),
        migrations.AlterField(
            model_name='tratamento',
            name='unidade_medida',
            field=models.CharField(choices=[('gt', 'Gota'), ('ml', 'ml'), ('cpm', 'Comprimido')], max_length=100, verbose_name='Unidade de Medida'),
        ),
    ]
