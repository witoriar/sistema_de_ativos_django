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
            return render(request, 'ativos/cadastrar.html', {
                'erro': 'Todos os campos são obrigatórios.',
                'tipos': Ativo.TIPO_ESCOLHA
            })

        obj = criar_ativo(None, hostname, responsavel, setor, tipo)

        Ativo.objects.create(
            hostname=obj.hostname,
            responsavel=obj.responsavel,
            setor=obj.setor,
            tipo=obj.tipo,
            dados_json=obj.to_dict()
        )

        return redirect('listar_ativos')

    return render(request, 'ativos/cadastrar.html', {
        'tipos': Ativo.TIPO_ESCOLHA
    })


def atualizar_ativo(request):
    ativo = None
    erro = None

    if request.method == 'POST':
        if 'id' in request.POST and 'hostname' not in request.POST:
            try:
                id_ativo = int(request.POST.get('id'))
                ativo = Ativo.objects.get(id=id_ativo)
            except (Ativo.DoesNotExist, ValueError):
                erro = 'Ativo não encontrado.'
            return render(request, 'ativos/atualizar.html', {
                'ativo': ativo,
                'tipos': Ativo.TIPO_ESCOLHA,
                'erro': erro
            })

        elif 'hostname' in request.POST:
            try:
                id_ativo = int(request.POST.get('id'))
                ativo = Ativo.objects.get(id=id_ativo)
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
            except (Ativo.DoesNotExist, ValueError):
                erro = 'Erro ao atualizar ativo.'

    return render(request, 'ativos/atualizar.html', {
        'ativo': ativo,
        'tipos': Ativo.TIPO_ESCOLHA,
        'erro': erro
    })


def deletar_ativo(request):
    ativo = None
    erro = None

    if request.method == 'POST':
        if 'id' in request.POST and 'confirmar' not in request.POST:
            try:
                id_ativo = int(request.POST.get('id'))
                ativo = Ativo.objects.get(id=id_ativo)
            except (Ativo.DoesNotExist, ValueError):
                erro = 'Ativo não encontrado.'
            return render(request, 'ativos/deletar.html', {
                'ativo': ativo,
                'erro': erro
            })

        elif 'confirmar' in request.POST:
            try:
                id_ativo = int(request.POST.get('id'))
                ativo = Ativo.objects.get(id=id_ativo)
                ativo.delete()
                return redirect('listar_ativos')
            except (Ativo.DoesNotExist, ValueError):
                erro = 'Erro ao deletar ativo.'

    return render(request, 'ativos/deletar.html', {
        'ativo': ativo,
        'erro': erro
    })


def cadastrar_vulnerabilidade(request):
    ativo = None
    erro = None

    if request.method == 'POST':
        if 'id' in request.POST and 'descricao' not in request.POST:
            try:
                id_ativo = int(request.POST.get('id'))
                ativo = Ativo.objects.get(id=id_ativo)
            except (Ativo.DoesNotExist, ValueError):
                erro = 'Ativo não encontrado.'
            return render(request, 'ativos/vulnerabilidade.html', {
                'ativo': ativo,
                'erro': erro,
                'severidades': Vulnerabilidade.SEVERIDADE_ESCOLHA,
                'status_opcoes': Vulnerabilidade.STATUS_ESCOLHA
            })

        elif 'descricao' in request.POST:
            try:
                id_ativo = int(request.POST.get('id'))
                ativo = Ativo.objects.get(id=id_ativo)
                descricao = request.POST.get('descricao', '').strip()
                severidade = request.POST.get('severidade', '').strip()
                status = request.POST.get('status', '').strip()

                if not descricao or not severidade or not status:
                    erro = 'Todos os campos são obrigatórios.'
                else:
                    Vulnerabilidade.objects.create(
                        ativo=ativo,
                        descricao=descricao,
                        severidade=severidade,
                        status=status
                    )
                    return redirect('listar_ativos')
            except (Ativo.DoesNotExist, ValueError):
                erro = 'Erro ao cadastrar vulnerabilidade.'

    return render(request, 'ativos/vulnerabilidade.html', {
        'ativo': ativo,
        'erro': erro,
        'severidades': Vulnerabilidade.SEVERIDADE_ESCOLHA,
        'status_opcoes': Vulnerabilidade.STATUS_ESCOLHA
    })


def visualizar_vulnerabilidades(request):
    ativo = None
    erro = None
    vulnerabilidades = None

    if request.method == 'POST':
        try:
            id_ativo = int(request.POST.get('id'))
            ativo = Ativo.objects.get(id=id_ativo)
            vulnerabilidades = Vulnerabilidade.objects.filter(ativo=ativo)
        except (Ativo.DoesNotExist, ValueError):
            erro = 'Ativo não encontrado.'

    return render(request, 'ativos/visualizar_vulnerabilidades.html', {
        'ativo': ativo,
        'erro': erro,
        'vulnerabilidades': vulnerabilidades
    })