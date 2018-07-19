from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet

from ishelf.content.models import (
    Author,
    Book,
)
from ishelf.content.serializers import (
    AuthorSerializer,
    BookSerializer,
)


# region Author

class AuthorViewSet(CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin,
                    GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# endregion

# region Book

class BookViewSet(CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin,
                  GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# endregion
