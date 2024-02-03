# Generated by Django 4.2.7 on 2023-12-05 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Название категории')),
            ],
        ),
        migrations.AddField(
            model_name='catalog',
            name='description',
            field=models.TextField(default='', verbose_name='Описание товара'),
        ),
        migrations.AddField(
            model_name='catalog',
            name='photo',
            field=models.ImageField(default=None, upload_to='photo/%Y/%m/%d/', verbose_name='Фото товара'),
        ),
        migrations.AddField(
            model_name='catalog',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.category', verbose_name='Категория'),
        ),
    ]
