# Generated by Django 3.1.3 on 2020-12-11 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20201211_1133'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AdminEmail',
            new_name='Recipient',
        ),
    ]
