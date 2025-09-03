from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # A linha abaixo foi corrigida para incluir as URLs da sua app 'plataforma'
    path('', include('plataforma.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
