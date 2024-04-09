from django.contrib import admin
from django.urls import path
# Imports para usar as imagens dentro de uma pasta no localhost do projeto
from django.conf import settings
from django.conf.urls.static import static
from cars.views import cars_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path('cars/', cars_view, name='cars_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
