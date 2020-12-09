from django.contrib import admin
from django.urls import path

from .views import index
from .views import send_mail

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('send/mail', send_mail, name='send_mail'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
