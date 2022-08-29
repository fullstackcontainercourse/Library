from django.contrib import admin
from django.urls import path
from . import views
from books.views import view_users_list, BookView, BookDetailView, UserListView, UserDetailView, BookListView, BookCreateView

app_name = 'books'
# /books/
urlpatterns = [
    path('users_v1/', views.view_users_list, name="view_users_v1"),
    # books/
    path('', BookView.as_view(), name="view_books"),
    # books/1
    path('<int:pk>/', BookDetailView.as_view(), name="view_book_by_id"),

    # users/
    path('users/', UserListView.as_view(), name="view_users"),

    # users/1
    path('users/<int:pk>/', UserDetailView.as_view(), name="options_on_users"),

    # users/1
    path('home/', views.index, name="indexview"),

    path('libraryhome/', BookListView.as_view(), name="book_details_home"),

    path('libraryhome/<int:pk>/', BookDetailView.as_view(),
         name="single_book_detail_view"),

    path('libraryhome/create/', BookCreateView.as_view(),
         name="single_book_create_view")

]
