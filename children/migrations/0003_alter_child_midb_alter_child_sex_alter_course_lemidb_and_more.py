# Generated by Django 4.1 on 2022-09-16 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('children', '0002_auto_20220610_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='midb',
            field=models.CharField(blank=True, choices=[('ቤተ ኪዳነምህረት', 'ቤተ ኪዳነምህረት'), ('ቤተ ዮሐንስ', 'ቤተ ዮሐንስ'), ('ቤተ መድኃኔአለም', 'ቤተ መድኃኔአለም'), ('ቤተ አረጋዊ', 'ቤተ አረጋዊ'), ('ወጣት', 'ወጣት')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='sex',
            field=models.CharField(choices=[('ወንድ', 'ወንድ'), ('ሴት', 'ሴት')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='lemidb',
            field=models.CharField(choices=[('ቤተ መድኃኔአለም', 'ቤተ መድኃኔአለም'), ('ቤተ አረጋዊ', 'ቤተ አረጋዊ'), ('ቤተ ኪዳነምህረት', 'ቤተ ኪዳነምህረት'), ('ቤተ ዮሐንስ', 'ቤተ ዮሐንስ')], max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='mark',
            name='midb',
            field=models.CharField(blank=True, choices=[('ቤተ መድኃኔአለም', 'ቤተ መድኃኔአለም'), ('ቤተ አረጋዊ', 'ቤተ አረጋዊ'), ('ቤተ ኪዳነምህረት', 'ቤተ ኪዳነምህረት'), ('ቤተ ዮሐንስ', 'ቤተ ዮሐንስ')], max_length=100, null=True),
        ),
    ]
