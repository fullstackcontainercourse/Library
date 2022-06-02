from django.urls import path

from . import views
from .views import BookView, BookDetailView, LoanListView

app_name = 'books'
urlpatterns = [
    path('details/', views.getBookDetails, name='index'),
    path('data/', views.getData, name='index12'),
    path('', views.books_display, name="books_display"),


    path('list', BookView.as_view(), name="books_viewlist"),
    path('<int:pk>/', BookDetailView.as_view(), name="books_viewbyid"),

    path('loans/', LoanListView.as_view(), name="loans_viewlist")

]
