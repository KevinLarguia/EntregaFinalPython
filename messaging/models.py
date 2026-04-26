from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sent_messages',
        verbose_name='Remitente'
    )
    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='received_messages',
        verbose_name='Destinatario'
    )
    subject = models.CharField(max_length=200, verbose_name='Asunto')
    content = models.TextField(verbose_name='Mensaje')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    read = models.BooleanField(default=False, verbose_name='Leído')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'

    def __str__(self):
        return f'{self.sender} → {self.receiver}: {self.subject}'
