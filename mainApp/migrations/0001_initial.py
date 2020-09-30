# Generated by Django 3.1.1 on 2020-09-29 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Заголовок статі')),
                ('text', models.TextField(verbose_name='Текст статі')),
                ('image', models.ImageField(upload_to='')),
                ('slug', models.SlugField(unique=True)),
                ('views', models.IntegerField()),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Articlesnew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('text', models.TextField()),
                ('category', models.TextField()),
                ('views', models.IntegerField()),
                ('img', models.ImageField(upload_to='')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Назва категорії')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='')),
                ('text', models.TextField(verbose_name='Текст статі')),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Назва мітки')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Текст заголовка')),
                ('btn_text', models.CharField(max_length=120, verbose_name='Текст кнопки')),
            ],
        ),
        migrations.CreateModel(
            name='Slider_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('slider_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.slider_info')),
            ],
        ),
        migrations.CreateModel(
            name='Cametn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor_name', models.CharField(max_length=120, verbose_name='Імя автора')),
                ('text', models.TextField(verbose_name='Текст')),
                ('articl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.article', verbose_name='Стаття')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.category', verbose_name='Категорія'),
        ),
        migrations.AddField(
            model_name='article',
            name='mark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.mark', verbose_name='Мітка'),
        ),
    ]
