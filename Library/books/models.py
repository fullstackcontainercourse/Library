from django.db import models
from django.urls import reverse

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100, default="TBD Title")
    type = models.CharField(max_length=20)
    isbn = models.CharField(max_length=20, default="ISBN0000")
    author = models.CharField(max_length=100)
    status = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('books:single_book_detail_view', args=[self.id])

    def __str__(self):
        return f"{self.isbn} - {self.title}"


class BookUser(models.Model):
    name = models.CharField(max_length=100, default="TBD Name")
    type = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default="ACTIVE")
    dept = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} - {self.dept}"
