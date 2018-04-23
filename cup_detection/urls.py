from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)