# Generated by Django 4.1.2 on 2022-11-28 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0009_tratamento_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dosestratamento',
            name='alarme',
            field=models.CharField(max_length=100),
        ),
    ]
