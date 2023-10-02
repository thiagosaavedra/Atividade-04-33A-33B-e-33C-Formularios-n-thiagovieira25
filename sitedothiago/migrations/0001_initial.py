# Generated by Django 3.2.13 on 2023-09-06 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='motivosArabia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dinheiro_colocado', models.CharField(max_length=50)),
                ('quantidade_jogadores', models.CharField(max_length=50)),
                ('quantidade_campeonatos', models.CharField(max_length=50)),
                ('clubes_famosos', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tabela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('elenco', models.CharField(max_length=70)),
                ('formacao', models.CharField(max_length=20)),
                ('capitao', models.CharField(max_length=50)),
            ],
        ),
    ]