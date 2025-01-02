from django.urls import path
from .views import jogo_dados

app_name = 'jogos'

urlpatterns = [
    path('jogos/jogo/<int:pk>',jogo_dados,name='jogo-detail')
]