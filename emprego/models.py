from django.db import models
from django.contrib.auth.models import User

class Empregos(models.Model):
    titulo = models.CharField(max_length=200)
    empresa = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_emprego = models.DateTimeField(verbose_name='Data do Criação')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data do Evento')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table='empregos'

    def __str__(self):
        return self.titulo

    def get_data_criacao(self):
        return self.data_criacao.strftime('%d/%m/%Y %H:%M')

    def get_data_input_emprego(self):
        return self.data_criacao.strftime('%Y-%m-%dT%H:%M')