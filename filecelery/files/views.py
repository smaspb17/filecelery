import time

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import File
from .serializers import FileSerializer
from .tasks import process_file


class FilePostView(CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
