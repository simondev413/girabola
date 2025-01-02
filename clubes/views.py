from django.shortcuts import render

from django.db.models import Sum, Q, F
from .models import Clube,Jogador
from jogos.models import Jogo

# Create your views here.


def classificacao(request):
    clubes = Clube.objects.all()
    
    tabela_classificacao = []
    for clube in clubes:
        gols_marcados = Jogo.objects.filter(clube_casa=clube).aggregate(Sum('gols_casa'))['gols_casa__sum'] or 0
        gols_marcados += Jogo.objects.filter(clube_fora=clube).aggregate(Sum('gols_fora'))['gols_fora__sum'] or 0

        gols_sofridos =Jogo.objects.filter(clube_casa=clube).aggregate(Sum('gols_fora'))['gols_fora__sum'] or 0
        gols_sofridos += Jogo.objects.filter(clube_fora=clube).aggregate(Sum('gols_casa'))['gols_casa__sum'] or 0

        vitorias = Jogo.objects.filter(
            Q(clube_casa=clube,gols_casa__gt=F('gols_fora'))|
            Q(clube_fora=clube,gols_fora__gt=F('gols_casa'))
        ).count()

        empates =Jogo.objects.filter(
            Q(clube_casa=clube,gols_casa=F('gols_fora'))|
            Q(clube_fora=clube,gols_fora=F('gols_casa'))
        ).count()

        derrotas = Jogo.objects.filter(
            Q(clube_casa=clube,gols_casa__lt=F('gols_fora'))|
            Q(clube_fora=clube,gols_fora__lt=F('gols_casa'))
        ).count()

        pontos = (vitorias*3) + empates
        
        partidas = Jogo.objects.filter(
            Q(clube_casa=clube) | Q(clube_fora=clube)
            ).count()
        
        ultimos_jogos = Jogo.objects.filter(
            Q(clube_casa=clube) | Q(clube_fora=clube)
            ).order_by('-data'[:5])
        
        ultimos_resultados = []
        for jogo in ultimos_jogos:
            if jogo.resultado == 'Casa' and jogo.clube_casa == clube:
                ultimos_resultados.insert(0,'win')
            elif jogo.resultado == 'Fora' and jogo.clube_fora == clube:
                ultimos_resultados.insert(0,'win')
            elif jogo.resultado == 'Empate':
                ultimos_resultados.insert(0,'draw')
            else:
                ultimos_resultados.insert(0,'loss')
        if len(ultimos_resultados) > 5:
            ultimos_resultados.pop(0)
        

        saldo_gols = gols_marcados - gols_sofridos
        tabela_classificacao.append({
            'pk':clube.pk,
            'avatar':clube.avatar,
            'clube_nome':clube.nome,
            'pontos':pontos,
            'vitorias':vitorias,
            'empates':empates,
            'derrotas':derrotas,
            'gols_marcados':gols_marcados,
            'gols_sofridos':gols_sofridos,
            'saldo_gols':saldo_gols,
            'ultimos_jogos':ultimos_resultados,
            'partidas':partidas
        })

        tabela_classificacao = sorted(
            tabela_classificacao,key=lambda x: (-x['pontos'],-x['saldo_gols'],-x['vitorias'])
        )

    context = {'ranking':tabela_classificacao}

    return render(request,'classificacao.html',context)

def mostrar_clubes(request):
    clubes = Clube.objects.all()
    context = {'clubes':clubes}
    return render(request,'clubes.html',context)

def clube_dados(request,pk):
    clube = Clube.objects.get(pk=pk)
    jogadores = Jogador.objects.filter(clube=clube).order_by('nome')
    context = {
        'clube':clube,
        'jogadores':jogadores,
        }
    return render(request,'clube.html',context)