from django.db import models


class IndexPage(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name='Заголовок'
    )
    subtitle = models.CharField(
        max_length=250,
        verbose_name='Подзаголовок'
    )
    about = models.TextField(
        verbose_name='О нас'
    )
    first_advantage_title = models.CharField(
        max_length=250,
        verbose_name='Заголовок первого преимущества'
    )
    first_advantage_text = models.TextField(
        verbose_name='Описание первого преимущества'
    )
    second_advantage_title = models.CharField(
        max_length=250,
        verbose_name='Заголовок второго преимущества'
    )
    second_advantage_text = models.TextField(
        verbose_name='Описание второго преимущества'
    )

    class Meta:
        verbose_name = 'Главная страница'
    
    def __str__(self):
        return 'Главная страница'


class Appeal(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Имя'
    )
    e_mail = models.EmailField(
        verbose_name='e-mail'
    )
    text = models.TextField(
        verbose_name='Сообщение'
    )

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'
    
    def __str__(self):
        return f'Обращение от {self.name}'
