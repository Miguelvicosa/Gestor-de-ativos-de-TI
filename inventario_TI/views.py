from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipamento
from .forms import EquipamentoForm

# View de Listagem
def lista_equipamentos(request):
    """
    Busca todos os equipamentos do banco e envia para o template
    """
    equipamentos = Equipamento.objects.all().select_related('categoria')
    contexto = {
        'equipamentos': equipamentos
    }
    return render(request, 'inventario_TI/lista_equipamentos.html', contexto)


# View de Detalhe
def detalhe_equipamento(request, id):
    """
    Recebe um ID pela URL, busca o equipamento específico e envia para o template
    """
    equipamento = get_object_or_404(Equipamento, id=id)
    contexto = {
        'equipamento': equipamento
    }
    return render(request, 'inventario_TI/detalhe_equipamento.html', contexto)


# View de Cadastro
def cadastro_equipamento(request):
    """
    Lida com GET e POST para cadastrar novos equipamentos
    GET: Exibe o formulário vazio
    POST: Valida, salva no banco e redireciona
    """
    if request.method == 'POST':
        # Usuário enviou dados do formulário
        form = EquipamentoForm(request.POST)
        
        if form.is_valid():
            # Dados válidos - salvar no banco
            form.save()
            # Redirecionar para a lista de equipamentos
            return redirect('lista_equipamentos')
    else:
        # Método GET - exibir formulário vazio
        form = EquipamentoForm()
    
    contexto = {
        'form': form
    }
    return render(request, 'inventario_TI/cadastro_equipamento.html', contexto)