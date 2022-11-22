# Generated by Django 4.1 on 2022-10-21 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_shelf_container'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('folder_key', models.CharField(max_length=100, unique=True)),
                ('no_of_file', models.IntegerField(blank=True, null=True)),
                ('cover', models.ImageField(blank=True, default='media/def_shelf.jpg', upload_to='media')),
            ],
        ),
    ]