# Generated by Django 4.1 on 2022-12-19 13:16

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gedam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('address', models.TextField(blank=True)),
                ('detail', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updateAt', models.DateTimeField(auto_now=True)),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Guzo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField(blank=True, null=True)),
                ('departure_date', models.DateField()),
                ('arrival_date', models.DateField()),
                ('cover', models.ImageField(blank=True, null=True, upload_to='media')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agelglot.gedam')),
            ],
        ),
        migrations.CreateModel(
            name='BookGuzo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('phone_no', models.CharField(max_length=30)),
                ('address', models.TextField(blank=True, null=True)),
                ('special_request', models.TextField(blank=True, null=True)),
                ('booking_id', models.CharField(max_length=50)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('guzo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agelglot.guzo')),
            ],
        ),
    ]