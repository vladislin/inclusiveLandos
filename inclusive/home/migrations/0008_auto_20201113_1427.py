# Generated by Django 3.1.3 on 2020-11-13 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_feedback'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': 'Фідбек', 'verbose_name_plural': 'Фідбеки'},
        ),
    ]