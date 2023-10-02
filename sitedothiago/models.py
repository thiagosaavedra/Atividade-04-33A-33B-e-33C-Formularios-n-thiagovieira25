from django.db import models

class Tabela(models.Model):
  title = models.CharField(max_length=50)
  cor = models.CharField(max_length=70)
  formacao = models.CharField(max_length=20)
  capitao = models.CharField(max_length=50)

class motivosArabia(models.Model):
  dinheiro_colocado = models.CharField(max_length=10000)
  quantidade_jogadores = models.CharField(max_length=50)
  quantidade_campeonatos = models.CharField(max_length=50)
  clubes_famosos = models.CharField(max_length=50)


