# Generated by Django 3.1.3 on 2020-11-13 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20201113_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='Singup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name="Ім'я")),
                ('surname', models.CharField(max_length=30, verbose_name='Прізвище')),
                ('phone', models.CharField(max_length=10, verbose_name='Номер телефону')),
                ('email', models.EmailField(max_length=254)),
                ('description', models.CharField(max_length=300, verbose_name='Коментар')),
            ],
        ),
    ]