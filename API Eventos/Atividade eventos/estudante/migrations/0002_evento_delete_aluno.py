# Generated by Django 5.1.7 on 2025-03-21 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('data_hora', models.DateTimeField()),
                ('local', models.CharField(blank=True, max_length=255, null=True)),
                ('categoria', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Aluno',
        ),
    ]
