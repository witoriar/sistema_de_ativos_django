from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_ativos, name='listar_ativos'),
    path('cadastrar/', views.cadastrar_ativo, name='cadastrar_ativo'),
    path('atualizar/', views.atualizar_ativo, name='atualizar_ativo'),
    path('deletar/', views.deletar_ativo, name='deletar_ativo'),
    path('vulnerabilidade/', views.cadastrar_vulnerabilidade, name='cadastrar_vulnerabilidade'),
    path('vulnerabilidades/', views.visualizar_vulnerabilidades, name='visualizar_vulnerabilidades'),
]