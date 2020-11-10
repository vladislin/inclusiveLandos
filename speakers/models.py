from django.db import models


# Create your models here.

class Speaker(models.Model):
    name = models.CharField(max_length=60, verbose_name="Прізвище та ім'я")
    description = models.CharField(max_length=300, verbose_name="Короткий текст")
    fb = models.CharField(max_length=150, verbose_name="Фб-профіль посилання")
    linkedin = models.CharField(max_length=150, verbose_name="Linkedin-профіль посилання")
    alt = models.CharField(max_length=300, verbose_name='Alt текст')
    image = models.ImageField(upload_to="speakers_pictures", verbose_name='Зображення')

    class Meta:
        verbose_name = 'Спікер'
        verbose_name_plural = 'Спікери'
