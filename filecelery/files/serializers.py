import mimetypes

from rest_framework.serializers import (
    ModelSerializer,
    ValidationError,
)

from .models import File

ALLOWED_TYPES = [
    'image/jpeg',
    'image/png',
    'text/plain',
    'application/pdf'
    'application/json',
    'text/x-python',
]


class FileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'file', 'uploaded_at', 'processed')

    def validate_file(self, value):
        file_type, _ = mimetypes.guess_type(value.name)
        if file_type not in ALLOWED_TYPES:
            raise ValidationError('Недопустимый тип файла')
        return value