from django.contrib import admin
from .models import Ativo, Vulnerabilidade

@admin.register(Ativo)
class AtivoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hostname', 'tipo', 'responsavel', 'setor']
    search_fields = ['hostname', 'responsavel']
    list_filter = ['tipo']


@admin.register(Vulnerabilidade)
class VulnerabilidadeAdmin(admin.ModelAdmin):
    list_display = ['id', 'ativo', 'severidade', 'status']
    list_filter = ['severidade', 'status']
