from django.urls import path
from .views import jogo_dados,index

app_name = 'jogos'

urlpatterns = [
    path('',index,name='jogos'),
    path('jogos/jogo/<int:pk>',jogo_dados,name='jogo-detail')
]