# Generated by Django 2.0.5 on 2018-05-15 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feira',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.BigIntegerField()),
                ('lat', models.BigIntegerField()),
                ('set_sens', models.BigIntegerField()),
                ('area_p', models.BigIntegerField()),
                ('cod_dist', models.IntegerField()),
                ('distrito', models.CharField(max_length=100)),
                ('cod_sub_pref', models.IntegerField()),
                ('sub_pref', models.CharField(max_length=100)),
                ('regiao5', models.CharField(max_length=20)),
                ('regiao8', models.CharField(max_length=20)),
                ('nome_feira', models.CharField(max_length=200)),
                ('registro', models.CharField(max_length=20)),
                ('logradouro', models.CharField(max_length=250)),
                ('numero', models.CharField(blank=True, max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('referencia', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
