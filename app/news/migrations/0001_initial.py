# Generated by Django 3.2 on 2022-05-30 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TegsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True, verbose_name='Название тега')),
            ],
        ),
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('image', models.ImageField(blank=True, upload_to='2022-05-30 18:07:31.740544-5592', verbose_name='Image')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('tegs', models.ManyToManyField(to='news.TegsModel')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
                'ordering': ['-create_at'],
            },
        ),
        migrations.CreateModel(
            name='AdditionalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='2022-05-30 18:07:31.7417849926', verbose_name='Image')),
                ('new', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.newsmodel', verbose_name='P')),
            ],
            options={
                'verbose_name': 'AddImage',
            },
        ),
    ]
