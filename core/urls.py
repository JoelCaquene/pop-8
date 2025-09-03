from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pop-8.urls')),  # Esta linha direciona a URL raiz para as URLs do seu app
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
