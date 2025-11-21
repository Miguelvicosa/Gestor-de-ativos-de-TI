from django.urls import path
from . import views

urlpatterns = [
    # View de Listagem - Página inicial que mostra todos os equipamentos
    path('', views.lista_equipamentos, name='lista_equipamentos'),
    
    # View de Detalhe - Mostra detalhes de um equipamento específico pelo ID
    path('equipamento/<int:id>/', views.detalhe_equipamento, name='detalhe_equipamento'),
    
    # View de Cadastro - Formulário para adicionar novo equipamento
    path('cadastro/', views.cadastro_equipamento, name='cadastro_equipamento'),
]