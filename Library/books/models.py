from django.db import models
from datetime import date

# Create your models here


class Book(models.Model):

    title = models.CharField(max_length=100, default="TBD title")
    type = models.CharField(max_length=30, null=True)
    isbn = models.CharField(max_length=20, default=0)
    author = models.CharField(max_length=100)

    def __str__(self):
        return f" {self.isbn} - {self.title} by {self.author}"


class Loan(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loanerName = models.CharField(max_length=100)
    loanDate = models.DateField("Loan Date", default=date.today)
    loanStatus = models.CharField(max_length=20)

    def __str__(self):
        return f" Loan id {self.id} - {self.loanerName} - {self.book} - {self.loanStatus}"
