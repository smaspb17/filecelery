import mimetypes
from celery import shared_task


@shared_task
def process_file(file_id):
    from files.models import File
    file = File.objects.get(id=file_id)
    file_type, _ = mimetypes.guess_type(file.file.name)
    # Обработка файлов в зависимости от типа
    if file_type.startswith('image/'):
        process_image(file)
    elif file_type == 'text/plain':
        process_text_file(file)
    elif file_type == 'application/pdf':
        process_pdf(file)
    elif file_type == 'application/json':
        process_json(file)
    elif file_type == 'text/x-python':
        process_python(file)
    file.processed = True
    file.save()
    return f'Файл id {file.id} обработан Celery!'


def process_image(file):
    # Логика обработки изображений
    pass


def process_text_file(file):
    # Логика обработки текстовых файлов
    pass


def process_pdf(file):
    # Логика обработки pdf-файлов
    pass


def process_json(file):
    # Логика обработки json-файлов
    pass


def process_python(file):
    # Логика обработки python-файлов
    pass