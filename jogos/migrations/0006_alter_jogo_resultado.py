# Generated by Django 5.1.4 on 2025-01-02 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogos', '0005_rename_resulatdo_jogo_resultado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogo',
            name='resultado',
            field=models.CharField(blank=True, choices=[('Casa', '1'), ('Fora', '2'), ('Empate', 'x')], max_length=20),
        ),
    ]