# Generated by Django 5.1.4 on 2025-01-02 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jogos', '0004_jogo_resulatdo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jogo',
            old_name='resulatdo',
            new_name='resultado',
        ),
    ]