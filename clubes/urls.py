from django.urls import path
from .views import classificacao,mostrar_clubes,clube_dados,dados_jogador

app_name = 'clubes'

urlpatterns = [
    path('classificacao',classificacao,name='ranking'),
    path('clubes',mostrar_clubes,name='clubes-list'),
    path('clubes/clube/<int:pk>',clube_dados,name='clube-detail'),
    path('clubes/clube/<int:clube_pk>/jogadores/<int:pk>',dados_jogador,name='jogador-detail'),
]