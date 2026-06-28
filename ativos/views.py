from django.shortcuts import render, get_object_or_404, redirect
from .models import Ativo, Vulnerabilidade
from .classes.subclasses import criar_ativo

def listar_ativos(request):
    ativos = Ativo.objects.all()
    return render(request, 'ativos/listar.html', {'ativos': ativos})

def cadastrar_ativo(request):
    if request.method == 'POST':
        hostname = request.POST.get('hostname', '').strip()
        responsavel = request.POST.get('responsavel', '').strip()
        setor = request.POST.get('setor', '').strip()
        tipo = request.POST.get('tipo', '').strip()

        if not hostname or not responsavel or not setor or not tipo:
            return render(request, 'ativos/cadastrar.html',{
                'erro': 'Todos os campos são obrigatórios.',
                'tipos': Ativo.TIPO_ESCOLHA
            })
        
        obj = criar_ativo(None, hostname, responsavel, setor, tipo)

        Ativo = Ativo.objects.create(
            hostname=obj.hostname,
            responsavel=obj.responsavel,
            setor=obj.setor,
            tipo=obj.tipo,
            dados_json=obj.to_dict()
        )

        return redirect('listar_ativos')
    
    return render(request, 'ativos/cadastrar.html',{
        'tipos': Ativo.TIPO_ESCOLHA
        })

def atualizar_ativo(request, id):
    ativo = get_object_or_404(Ativo, id=id)

    if request.method == 'POST':
        ativo.hostname = request.POST.get('hostname', '').strip()
        ativo.responsavel = request.POST.get('responsavel', '').strip()
        ativo.setor = request.POST.get('setor', '').strip()
        ativo.tipo = request.POST.get('tipo', '').strip()
        ativo.dados_json = {
            'hostname': ativo.hostname,
            'responsavel': ativo.responsavel,
            'setor': ativo.setor,
            'tipo': ativo.tipo,
        }
        ativo.save()
        return redirect('listar_ativos')
    
    return render(request, 'ativos/atualizar.html',{
        'ativo': ativo,
        'tipos': Ativo.TIPO_ESCOLHA
    })

def deletar_ativo(request, id):
    Ativo = get_object_or_404(Ativo, id=id)

    if request.method == 'POST':
        Ativo.delete()
        return redirect('listar_ativos')
    
    return render(request, 'ativos/deletar.html', {'ativo': ativo})

def cadastrar_vulnerabilidade(request, id):
    ativo = get_object_or_404(Ativo, id=id)

    if request.method == 'POST':
        descricao= request.POST.get('descricao', '').strip()
        severidade = request.POST.get('severidade', '').strip()
        status = request.POST.get('status', '').strip()
        

        if not descricao or not severidade or not status:
            return render(request, 'ativos/vulnerabilidade.html',{
                'ativo': ativo,
                'erro': 'Todos os campos são obrigatórios.',
                'severidades': Vulnerabilidade.SEVERIDADE_ESCOLHA,
                'status_opcoes': Vulnerabilidade.STATUS_ESCOLHA
            })
        
        Vulnerabilidade.objects.create(
            ativo=ativo,
            descricao=descricao,
            severidade=severidade,
            status=status
        )

        return redirect('listar_ativos')
        
    return render(request, 'ativos/vulnerabilidade.html', {
        'ativo': ativo,
        'severidades': Vulnerabilidade.SEVERIDADE_CHOICES,
        'status_opcoes': Vulnerabilidade.STATUS_CHOICES
    })

def visualizar_vulnerabilidades(request, id):
    ativo = get_object_or_404(Ativo, id=id)
    vulnerabilidades = Vulnerabilidade.objects.filter(ativo=ativo)
    return render(request, 'ativos/visualizar_vulnerabilidades.html', {
        'ativo': ativo,
        'vulnerabilidades': vulnerabilidades
    })