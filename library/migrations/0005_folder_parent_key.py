# Generated by Django 4.1 on 2022-10-21 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_folder'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='parent_key',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
