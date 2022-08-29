
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from books.models import Book, BookUser
from .serializers import BookSerializer, BookUserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from .forms import BookCreateForm

import json

from books.serializers import BookSerializer


# Create your views here.


# def view_users_list(request):
#     user_data = BookUser.objects.all()
#     return HttpResponse(user_data)

def view_users_list(request):
    # iterable
    user_data = BookUser.objects.all()
    #  html
    user_template = loader.get_template("UserDetails.html")
    # dictionary data
    context = {'books_user_data': user_data}
    # merging
    html_data = user_template.render(context)
    # rendered
    # <html>
    # ....
    # </html>
    return HttpResponse(html_data)


class BookView(APIView):
    def get(self, request):
        book_list = Book.objects.all()
        serializer = BookSerializer(book_list, many=True)
        return Response(serializer.data)


class BookDetailView(APIView):
    def get(self, request, pk):
        book_list = Book.objects.get(pk=pk)
        serializer = BookSerializer(book_list)
        return Response(serializer.data)


class UserListView(generics.ListCreateAPIView):
    queryset = BookUser.objects.all()
    serializer_class = BookUserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookUser.objects.all()
    serializer_class = BookUserSerializer


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()

    # The 'all()' is implied by default.
    num_authors = BookUser.objects.count()

    context = {
        'num_books': num_books,

        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'LibraryHomePage.html', context=context)


# ListView example to display all books just with ListView & 3 lines of code
class BookListView (ListView):
    template_name = "index.html"
    queryset = Book.objects.all()
    context_object_name = 'books'





class BookDetailView (DetailView):
    model = Book
    template_name = "book_detail.html"






class BookCreateView(CreateView):
    template_name = 'book_create.html'
    form_class = BookCreateForm
