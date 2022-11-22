# Generated by Django 3.2.6 on 2022-06-10 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('children', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=100, null=True, unique=True)),
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('lemidb', models.CharField(max_length=100, null=True, unique=True)),
                ('attachment', models.FileField(upload_to='media')),
            ],
        ),
        migrations.AlterField(
            model_name='child',
            name='dikuna',
            field=models.CharField(blank=True, choices=[('እጩ ዲያቆን', 'እጩ ዲያቆን'), ('-ዲያቆን', '-ዲያቆን')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='midb',
            field=models.CharField(blank=True, choices=[('ቤተ አረጋዊ', 'ቤተ አረጋዊ'), ('ቤተ ዮሐንስ', 'ቤተ ዮሐንስ'), ('ቤተ መድኃኔአለም', 'ቤተ መድኃኔአለም'), ('ቤተ ኪዳነምህረት', 'ቤተ ኪዳነምህረት')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='sex',
            field=models.CharField(choices=[('ሴት', 'ሴት'), ('ወንድ', 'ወንድ')], max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('midb', models.CharField(blank=True, choices=[('ቤተ አረጋዊ', 'ቤተ አረጋዊ'), ('ቤተ ዮሐንስ', 'ቤተ ዮሐንስ'), ('ቤተ መድኃኔአለም', 'ቤተ መድኃኔአለም'), ('ቤተ ኪዳነምህረት', 'ቤተ ኪዳነምህረት')], max_length=100, null=True)),
                ('assessment', models.IntegerField()),
                ('final', models.IntegerField(blank=True, null=True)),
                ('total', models.IntegerField(blank=True, editable=False, null=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='children.course')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='children.child')),
            ],
        ),
    ]