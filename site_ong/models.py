from django.db import models


class Voluntario(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    periodo = models.CharField(max_length=50)
    projetos = models.JSONField(default=list)
    horas = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, default="Pendente")
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
