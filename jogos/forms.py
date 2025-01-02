from django import forms
from .models import Jogo
from clubes.models import Jogador

class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Inicializar os campos sem restrição, eles serão atualizados via JS
        self.fields['jogadores_casa'].queryset = Jogador.objects.none()
        self.fields['jogadores_fora'].queryset = Jogador.objects.none()

        if 'clube_casa' in self.data:
            try:
                clube_casa_id = int(self.data.get('clube_casa'))
                self.fields['jogadores_casa'].queryset = Jogador.objects.filter(clube_id=clube_casa_id)
            except (ValueError, TypeError):
                pass

        if 'clube_fora' in self.data:
            try:
                clube_fora_id = int(self.data.get('clube_fora'))
                self.fields['jogadores_fora'].queryset = Jogador.objects.filter(clube_id=clube_fora_id)
            except (ValueError, TypeError):
                pass

        if self.instance.pk:
            self.fields['jogadores_casa'].queryset = Jogador.objects.filter(clube=self.instance.clube_casa)
            self.fields['jogadores_fora'].queryset = Jogador.objects.filter(clube=self.instance.clube_fora)
