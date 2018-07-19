from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from ishelf.content.views import (
    AuthorViewSet,
    BookViewSet,
)

router = routers.DefaultRouter()
router.register("authors", AuthorViewSet)
router.register("books", BookViewSet)

urlpatterns = [
    path("", include(router.urls))
]
