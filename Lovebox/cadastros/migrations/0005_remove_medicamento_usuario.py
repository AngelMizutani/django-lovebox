# Generated by Django 4.0.3 on 2022-08-29 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0004_medicamento_usuario_perfil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicamento',
            name='usuario',
        ),
    ]
