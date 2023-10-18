from django.urls import path, include

from .views import FilePostView

urlpatterns = [
    path('upload/', FilePostView.as_view(), name='file-upload'),
]
