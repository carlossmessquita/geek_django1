# Generated by Django 3.2.13 on 2022-05-17 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Nome')),
                ('nota', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Nota')),
                ('alunos', models.IntegerField(verbose_name='QTD. de Alunos')),
            ],
        ),
    ]