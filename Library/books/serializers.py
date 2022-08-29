from books.models import Book, BookUser
from rest_framework.serializers import ModelSerializer


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class BookUserSerializer(ModelSerializer):
    class Meta:
        model = BookUser
        fields = "__all__"
       
