from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import home, create

urlpatterns = [
    path('create', create, name='create')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
