from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Clube(models.Model):
    nome = models.CharField(max_length=180)
    estadio = models.CharField(max_length=180)
    vitorias = models.IntegerField()
    derrotas = models.IntegerField()
    empates = models.IntegerField()
    gols_feitos = models.IntegerField()
    gols_sofridos = models.IntegerField()
    avatar = models.ImageField(upload_to='media')
    treinador = models.CharField(max_length=120,null=True,blank=True)

    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Clube'
        verbose_name_plural = 'Clubes'
        ordering = ['nome']
    
class Jogador(models.Model):
    POSICAO = [(
        'Guarda-Redes','GD'),
        ('Defesa','DF'),
        ('Meio-campo','MD'),
        ('Avançado','AV') ]
        
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    clube = models.ForeignKey(Clube, on_delete = models.CASCADE)
    posicao = models.CharField(max_length=20,choices=POSICAO)
    numero = models.IntegerField()
    gols_marcados = models.IntegerField()
    is_capitao = models.BooleanField(default=False)
    
    
    class Meta:
        verbose_name = 'Jogador'
        verbose_name_plural = 'Jogadores'

    def save(self,*args,**kwargs):
        if self.is_capitao :
            existe_capitao =Jogador.objects.filter(clube=self.clube,is_capitao=True).exclude(id=self.id).exists()
            if existe_capitao:
                raise ValidationError(f'O clube já possui um capitão.')
        
        super().save(*args,**kwargs)

    def __str__(self):
        return f'{self.nome} {self.numero} - {self.posicao} ({self.clube.nome})'
        