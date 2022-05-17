# Generated by Django 3.2.13 on 2022-05-17 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aula',
            name='alunos',
        ),
        migrations.AddField(
            model_name='aula',
            name='participantes',
            field=models.IntegerField(default=0, verbose_name='QTD. de Participantes'),
            preserve_default=False,
        ),
    ]