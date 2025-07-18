from django.db import models


class PublishedModel(models.Model):
    """Абстрактная модель. Добвляет флаг is_published."""
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликована'
        # help_text='Запись опубликована'
    )

    class Meta:
        abstract = True

