from django.urls import path
from core import views as core_views


urlpatterns = [
    path('generate-document/', core_views.GenerateDocumentView.as_view(), name='generate_document'),
]