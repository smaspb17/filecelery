from celery import shared_task


@shared_task
def process_file(file_id):
    from files.models import File
    file = File.objects.get(id=file_id)
    # Здесь можно вставить обработку файла, например, какие-то вычисления или манипуляции с данными.
    file.processed = True
    file.save()
    return f'Файл id {file.id} обработан Celery!'
