# Generated by Django 4.1 on 2022-09-05 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evclidapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('subtitle', models.CharField(max_length=250, verbose_name='Подзаголовок')),
                ('about', models.TextField(verbose_name='О нас')),
                ('first_advantage_title', models.CharField(max_length=250, verbose_name='Заголовок первого преимущества')),
                ('first_advantage_text', models.TextField(verbose_name='Описание первого преимущества')),
                ('second_advantage_title', models.CharField(max_length=250, verbose_name='Заголовок второго преимущества')),
                ('second_advantage_text', models.TextField(verbose_name='Описание второго преимущества')),
            ],
        ),
    ]
