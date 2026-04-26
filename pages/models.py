from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    subtitle = models.CharField(max_length=300, blank=True, verbose_name='Subtítulo')
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField(upload_to='pages/', blank=True, null=True, verbose_name='Imagen')
    created_at = models.DateField(auto_now_add=True, verbose_name='Fecha de creación')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='pages',
        verbose_name='Autor'
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'

    def __str__(self):
        return self.title
