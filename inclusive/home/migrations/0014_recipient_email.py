# Generated by Django 3.1.3 on 2020-12-11 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20201211_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipient',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email користувача'),
        ),
    ]
