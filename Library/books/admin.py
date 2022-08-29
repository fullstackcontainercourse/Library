from django.contrib import admin
from .models import BookUser, Book

# Register your models here.
admin.site.register(BookUser)
admin.site.register(Book)
