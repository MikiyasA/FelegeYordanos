# Generated by Django 4.1 on 2022-12-24 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agelglot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guzo',
            name='cover',
        ),
        migrations.AddField(
            model_name='gedam',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='bookguzo',
            name='booking_id',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
