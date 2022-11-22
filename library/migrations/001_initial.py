# Generated by Django 3.2.6 on 2022-06-04 11:45

from django.db import migrations, models
import django.db.models.deletion
import library.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('cover', models.ImageField(blank=True, default='media/def_cont.jpg', upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('no_of_books', models.IntegerField(blank=True, null=True)),
                ('cover', models.ImageField(blank=True, default='media/def_shelf.jpg', upload_to='media')),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.container')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_id', models.CharField(default=library.models.book_idno, editable=False, max_length=45, unique=True)),
                ('file', models.FileField(null=True, upload_to='media')),
                ('file_name', models.CharField(max_length=1000)),
                ('edition', models.CharField(blank=True, max_length=1000, null=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('cover', models.ImageField(blank=True, default='media/def.jpg', upload_to='media')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('shelf_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='library.shelf')),
            ],
        ),
    ]