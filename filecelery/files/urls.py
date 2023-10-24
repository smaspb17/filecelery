from django.urls import path, include

from .views import FileCreateView, FileListView

urlpatterns = [
    path('upload/', FileCreateView.as_view(), name='file-upload'),
    path('files/', FileListView.as_view(), name='file-files'),
]
