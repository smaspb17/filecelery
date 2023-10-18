from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import process_file

class File(models.Model):
    file = models.FileField(
        upload_to='files',
        help_text='Загрузите файл',
        verbose_name='Файл',
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время загрузки файла',
    )
    processed = models.BooleanField(
        default=False,
        verbose_name='Обработан ли файл',
    )


# сигнал-вызов задачи для Celery
@receiver(post_save, sender=File)
def file_post_save(sender, instance, created, **kwargs):
    if created:
        process_file.delay(instance.id)
