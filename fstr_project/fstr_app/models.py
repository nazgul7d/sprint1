from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class Pass(models.Model):
    beauty_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255)
    connect = models.CharField(max_length=255)
    add_time = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('pending', 'На модерации'),
        ('accepted', 'Принят'),
        ('rejected', 'Отклонен'),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')

    # Географические координаты
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()

    # Уровень сложности по сезонам
    winter_level = models.CharField(max_length=50, blank=True)
    summer_level = models.CharField(max_length=50, blank=True)
    autumn_level = models.CharField(max_length=50, blank=True)
    spring_level = models.CharField(max_length=50, blank=True)

    # Информация о пользователе
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Перевал'
        verbose_name_plural = 'Перевалы'

    # Поле для хранения JSON с изображениями
    images = models.JSONField()

    def __str__(self):
        return self.title