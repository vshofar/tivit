# Generated by Django 2.0.5 on 2018-05-15 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feiras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feira',
            name='registro',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]