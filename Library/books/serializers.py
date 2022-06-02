from rest_framework.serializers import ModelSerializer
from books.models import Book, Loan


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class LoanSerializer(ModelSerializer):
    class Meta:
        model = Loan
        fields = "__all__"
