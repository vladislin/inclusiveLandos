# Generated by Django 3.1.3 on 2020-12-10 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20201210_1718'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SectionOff',
            new_name='Section',
        ),
        migrations.AlterModelOptions(
            name='singup',
            options={'verbose_name': 'Реєстрація', 'verbose_name_plural': 'Реєстрації'},
        ),
    ]
