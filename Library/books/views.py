from django.shortcuts import render
from django.http import HttpResponse
from books.forms import BookForm
from books.models import Book, Loan
import json
from django.views import View
from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoanSerializer
from django.template import loader

# Create your views here.


def books_display(request):
    books_data = Book.objects.all()
    template = loader.get_template("books/bookssubpage.html")
    context = {"book_data": books_data}
    html_content = template.render(context)
    return HttpResponse(html_content)

# Class based view example


class BookView(View):
    def get(self, request):
        booksList = get_list_or_404(Book)
        bk_json = json.dumps([
            dict(id=bk.id,
                 name=bk.title
                 )
            for bk in booksList
        ])
        return HttpResponse(bk_json, content_type="application/json")


class BookDetailView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        bk_json = json.dumps(
            dict(id=book.id,
                 name=book.title
                 )
        )
        return HttpResponse(bk_json, content_type="application/json")


class LoanListView(APIView):
    def get(self, request):
        loans_list = get_list_or_404(Loan)
        serializer = LoanSerializer(loans_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = {
            'book': request.data.get('book'),
            'loanerName': request.data.get('book'),
            'loanStatus': 'ACTIVE'

        }
        serializer = LoanSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data)


def getData(request):
    output = Book.objects.all()

    return HttpResponse(output)


def getBookDetails(request, bookId):
    return HttpResponse("You're looking at question %s." % bookId)
