from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Campeonato(models.Model):
    nome = models.CharField(max_length=120)
    temporada = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.nome} - {self.temporada}'

class Jogo(models.Model):
    campeonato = models.ForeignKey(
        Campeonato,
        on_delete=models.CASCADE,
        related_name='jogos'
    )
    clube_casa = models.ForeignKey(
        'clubes.Clube',
        on_delete=models.CASCADE,
        related_name='jogos_casa'
    )
    clube_fora = models.ForeignKey(
        'clubes.Clube',
        on_delete=models.CASCADE,
        related_name='jogos_fora'
    )
    estadio = models.CharField(max_length=120)
    data = models.DateTimeField()
    gols_casa = models.IntegerField()
    gols_fora = models.IntegerField()
    jogadores_casa = models.ManyToManyField(
        'clubes.Jogador',
        related_name='partidas_casa',
        limit_choices_to={'clube__isnull': False},
    )
    jogadores_fora = models.ManyToManyField(
        'clubes.Jogador',
        related_name='partidas_fora',
        limit_choices_to={'clube__isnull': False}
    )
    guarda_rede_casa = models.ForeignKey(
        'clubes.Jogador',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='partida_casa_guarda_redes',
        limit_choices_to={'posicao': 'Guarda-Redes'}
    )
    guarda_rede_fora = models.ForeignKey(
        'clubes.Jogador',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='partida_fora_guarda_redes',
        limit_choices_to={'posicao': 'Guarda-Redes'}
    )
    STATUS = [
        ('Realizado', 'Realizado'),
        ('Não Realizado', 'Não Realizado'),
        ('Adiado', 'Adiado'),
        ('Cancelado', 'Cancelado')
    ]
    status = models.CharField(max_length=20, choices=STATUS, default='Não Realizado')
    resultado = models.CharField(max_length=20,choices=[('Casa','1'),('Fora','2'),('Empate','x')],blank=True)

    def __str__(self) -> str:
        return f'{self.clube_casa} vs {self.clube_fora} - {self.gols_casa}:{self.gols_fora} ({self.status})'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['campeonato', 'clube_casa', 'clube_fora'],
                name='unique_jogo_mesmo_campeonato'
            )
        ]
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'
        ordering = ['-data']

    def clean(self):
        # Validação personalizada para garantir que os clubes não joguem mais de duas vezes
        jogos_existentes = Jogo.objects.filter(
            campeonato=self.campeonato,
            clube_casa__in=[self.clube_casa, self.clube_fora],
            clube_fora__in=[self.clube_casa, self.clube_fora],
            status='Realizado'
        ).count()

        if jogos_existentes >= 2:
            raise ValidationError(
                f"Os clubes {self.clube_casa} e {self.clube_fora} já jogaram duas vezes neste campeonato."
            )

    def save(self, *args, **kwargs):
        self.clean()
        if self.gols_casa > self.gols_fora:
            self.resultado = 'Casa'
        elif self.gols_fora < self.gols_casa:
            self.resultado = 'Fora'
        else:
            if self.gols_casa == self.gols_fora:
                self.resultado = 'Empate'
        
        super().save(*args, **kwargs)

        

class Golo(models.Model):
    TIPO = [
        ('Cabeça','Cabeça'),
        ('Remate','Remate'),
        ('Livre','Livre'),
        ('Pênalti','Pênalti'),
        ('Acrobático','Acrobático')
        ]
    jogador = models.ForeignKey('clubes.Jogador',on_delete=models.CASCADE)
    tempo = models.TimeField(auto_now_add=True)
    partida = models.ForeignKey(Jogo,on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20,choices=TIPO)
    
    def __str__(self) -> str:
        return f'{self.jogador.nome} - {self.tipo} ({self.tempo.minute}:{self.tempo.second}) | {self.partida}'
    
    class Meta:
        verbose_name = 'Golo'
        verbose_name_plural = 'Golos'
        ordering = ['-tempo']
    
    