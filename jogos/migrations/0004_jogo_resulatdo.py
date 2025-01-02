# Generated by Django 5.1.4 on 2025-01-02 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogos', '0003_remove_jogo_unique_jogo_mesmo_campeonato_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogo',
            name='resulatdo',
            field=models.CharField(choices=[('Casa', '1'), ('Fora', '2'), ('Empate', 'x')], default=0, max_length=20),
            preserve_default=False,
        ),
    ]
