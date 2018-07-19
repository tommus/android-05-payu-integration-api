from rest_framework.serializers import ModelSerializer

from ishelf.content.models import (
    Author,
    Book,
)


# region Author

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


# endregion

# region Book

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

# endregion
