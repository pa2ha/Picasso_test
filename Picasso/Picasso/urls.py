from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from main.views import ListFilesViewSet, UploadFileViewSet
from rest_framework.routers import DefaultRouter

v1_router = DefaultRouter()
v1_router.register('files', ListFilesViewSet, basename='file-list')
v1_router.register('upload', UploadFileViewSet, basename='file-upload')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(v1_router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
