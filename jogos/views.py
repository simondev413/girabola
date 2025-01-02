from django.shortcuts import render
from .models import Jogo,Golo
from clubes.models import Jogador

# Create your views here.
def jogo_dados(request,pk):
    jogo = Jogo.objects.get(pk=pk)
    golos = Golo.objects.filter(partida=jogo)
    golos_fora = []
    golos_casa= []
    jogadores_casa = jogo.jogadores_casa.all()
    jogadores_fora = jogo.jogadores_fora.all()

    for golo in golos:
        if golo.jogador.clube == jogo.clube_casa:
            golos_casa.append(golo)
        elif golo.jogador.clube == jogo.clube_fora:
            golos_fora.append(golo)
        
    # for jogadores in jogo.jogadores_fora.values_list('pk'):
    #     for jogador in jogadores:
    #         jogador = Jogador.objects.get(pk=jogador)
    #         jogadores_casa.append(jogador)
    
    # for jogadores in jogo.jogadores_casa.values_list('pk'):
    #     for jogador in jogadores:
    #         jogadores_fora.append(Jogador.objects.get(pk=jogador))
    
    context = {
        'jogo':jogo,
        'golos':golos,
        'golos_fora':golos_fora,
        'golos_casa':golos_casa,
        'jogadores_casa':jogadores_casa,
        'jogadores_fora':jogadores_fora}
    return render(request,'jogo_detail.html',context)
