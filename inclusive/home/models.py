from django.db import models
from django.utils import timezone


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=80, verbose_name='Заголовок')
    description = models.CharField(max_length=300, verbose_name='Опис')
    image = models.ImageField(upload_to="news_pictures", verbose_name='Зображення')
    date = models.DateTimeField(default=timezone.now, verbose_name='Дата публікації')
    alt = models.CharField(max_length=300, verbose_name='Alt текст')
    is_hidden = models.BooleanField(verbose_name='Показувати поле', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Новини'
        verbose_name = 'Новина'


class Speaker(models.Model):
    name = models.CharField(max_length=100, verbose_name="Прізвище та ім'я")
    description = models.CharField(max_length=500, verbose_name="Короткий текст")
    fb = models.CharField(max_length=150, verbose_name="Фб-профіль посилання")
    linkedin = models.CharField(max_length=150, verbose_name="Linkedin-профіль посилання")
    alt = models.CharField(max_length=300, verbose_name='Alt текст')
    image = models.ImageField(upload_to="speakers_pictures", verbose_name='Зображення')

    class Meta:
        verbose_name = 'Спікер'
        verbose_name_plural = 'Спікери'

    def __str__(self):
        return self.name


class Section(models.Model):
    section_name = models.CharField(max_length=30, verbose_name="Ім'я секції", null=True)
    is_hidden = models.BooleanField(verbose_name='Показувати секцію?')

    class Meta:
        verbose_name = 'Секція'
        verbose_name_plural = 'Секції'

    def __str__(self):
        return self.section_name


class Feedback(models.Model):
    username = models.CharField(max_length=100, verbose_name="Ім'я користувача")
    description = models.CharField(max_length=500, verbose_name="Відгук")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Фідбек'
        verbose_name_plural = 'Фідбеки'


class Singup(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ім'я")
    surname = models.CharField(max_length=100, verbose_name="Прізвище")
    phone = models.CharField(max_length=12, verbose_name="Номер телефону")
    email = models.EmailField()
    description = models.CharField(max_length=500, verbose_name="Коментар")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Реєстрація'
        verbose_name_plural = 'Реєстрації'


class Recipient(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ім'я")
    email = models.EmailField(verbose_name='Email користувача', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отримувач'
        verbose_name_plural = 'Отримувачі'
