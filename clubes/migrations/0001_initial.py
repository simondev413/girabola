# Generated by Django 5.1.4 on 2024-12-30 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=180)),
                ('estadio', models.CharField(max_length=180)),
                ('vitorias', models.IntegerField()),
                ('derrotas', models.IntegerField()),
                ('empates', models.IntegerField()),
                ('gols_feitos', models.IntegerField()),
                ('gols_sofridos', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Clube',
                'verbose_name_plural': 'Clubes',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('posicao', models.CharField(choices=[('Guarda-Redes', 'Guarda-Redes'), ('Defesa Central', 'Defesa Central'), ('Lateral Esquerda', 'Lateral Esquerda'), ('LAteral Direita', 'Lateral Direita'), ('Meio Central', 'Meio Central'), ('Meia Defensivo', 'Meia Defensivo'), ('Meia Ofensiva', 'Meia Ofensiva'), ('Ponta Direita', 'Ponta Direita'), ('Ponta Esquerda', 'Ponta Esquerda')], max_length=20)),
                ('numero', models.IntegerField()),
                ('gols_marcados', models.IntegerField()),
                ('capitao', models.BooleanField(default=False)),
                ('clube', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubes.clube')),
            ],
            options={
                'verbose_name': 'Jogador',
                'verbose_name_plural': 'Jogadores',
            },
        ),
    ]
