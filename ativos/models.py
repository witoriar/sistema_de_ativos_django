from django.db import models

class Ativo(models.Model):
    
    TIPO_ESCOLHA = [
        ('SERVIDOR', 'servidor'),
        ('NOTEBOOK', 'notebook'),
        ('ROTEADOR', 'roteador'),
        ('APLICACAO_WEB', 'aplicacao web'),
    ]

    hostname = models.CharField(max_length=100)
    responsavel =  models.CharField(max_length=100)
    setor =  models.CharField(max_length=100)
    tipo =   tipo = models.CharField(max_length=20, choices=TIPO_ESCOLHA)
    dados_json = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.tipo} {self.hostname}"
    
    class Meta:
        verbose_name = 'Ativo'
        verbose_name_plural = 'Ativos'


class Vulnerabilidade(models.Model):

    SEVERIDADE_ESCOLHA = [
        ('BAIXA', 'Baixa'),
        ('MEDIA', 'Média'),
        ('ALTA', 'Alta'),
        ('CRITICA', 'Crítica'),
    ]

    STATUS_ESCOLHA = [
        ('ABERTA', 'Aberta'),
        ('EM_TRATAMENTO', 'Em Tratamento'),
        ('CORRIGIDA', 'Corrigida'),
        ('ACEITA', 'Aceita com Risco'),
    ]

    ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE, related_name='vulnerabilidades')
    descricao = models.TextField()
    severidade = models.CharField(max_length=20, choices=SEVERIDADE_ESCOLHA)
    status = models.CharField(max_length=20, choices=STATUS_ESCOLHA)

    def __str__(self):
        return f"{self.severidade} - {self.descricao[:50]}"
    
    class Meta:
        verbose_name = 'Vulnerabilidade'
        verbose_name_plural = 'Vulnerabilidades'