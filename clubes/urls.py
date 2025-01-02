from django.urls import path
from .views import classificacao,mostrar_clubes,clube_dados

app_name = 'clubes'

urlpatterns = [
    path('classificacao',classificacao,name='ranking'),
    path('clubes',mostrar_clubes,name='clubes-list'),
    path('clubes/clube/<int:pk>',clube_dados,name='clube-detail'),
]