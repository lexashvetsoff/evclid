from cgitb import text
import email
from django.db import models

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
