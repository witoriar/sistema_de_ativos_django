from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_ativos, name='listar_ativos'),
    path('cadastrar/', views.cadastrar_ativo, name='cadastrar_ativo'),
    path('atualizar/<int:id>/', views.atualizar_ativo, name='atualizar_ativo'),
    path('deletar/<int:id>/', views.deletar_ativo, name='deletar_ativo'),
    path('vulnerabilidade/<int:id>/', views.cadastrar_vulnerabilidade, name='cadastrar_vulnerabilidade'),
    path('vulnerabilidades/<int:id>/', views.visualizar_vulnerabilidades, name='visualizar_vulnerabilidades'),
]