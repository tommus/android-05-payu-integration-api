from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/content/", include(("ishelf.content.urls", "content"))),
    path("api/docs/", get_swagger_view(title="iShelf API")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = "iShelf API"
admin.site.site_header = "iShelf API"
