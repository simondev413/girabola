from django.contrib import admin
from .models import Jogo,Golo,Campeonato
from  .forms import JogoForm


class JogoAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'jogadores_casa':
            # Filtra os jogadores apenas do clube da casa
            if hasattr(request, '_obj_') and request._obj_:
                kwargs['queryset'] = db_field.related_model.objects.filter(clube=request._obj_.clube_casa)
        elif db_field.name == 'jogadores_fora':
            # Filtra os jogadores apenas do clube de fora
            if hasattr(request, '_obj_') and request._obj_:
                kwargs['queryset'] = db_field.related_model.objects.filter(clube=request._obj_.clube_fora)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def get_form(self, request, obj=None, **kwargs):
        # Passa o objeto atual para o request para usarmos no filtro
        request._obj_ = obj
        return super().get_form(request, obj, **kwargs)

admin.site.register(Jogo, JogoAdmin)
admin.site.register(Golo)
admin.site.register(Campeonato)