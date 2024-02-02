from celery import shared_task

from .models import File


@shared_task
def process_file(file_id):
    file_obj = File.objects.get(pk=file_id)
    file_path = file_obj.file.path
    if file_path.endswith('.jpg') or file_path.endswith('.png'):
        processed = process_image(file_obj)
    elif file_path.endswith('.txt'):
        processed = process_text_file(file_obj)
    elif file_path.endswith('.pdf'):
        processed = process_pdf(file_obj)
    else:
        processed = False

    if processed:
        file_obj.processed = True
        file_obj.save()


# Функции обработки различных типов файлов
def process_image(file_obj):
    # здесь происходит нужная обработка изображения
    return True  # возвращаем True после успешной обработки


def process_text_file(file_obj):

    # здесь происходит нужная обработка текста
    return True


def process_pdf(file_obj):
    # здесь происходит нужная обработка PDF

    return True

# можно расширять как требует проект
