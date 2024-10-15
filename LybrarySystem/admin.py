from django.contrib import admin
from .models import Book
from .models import Reader
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ['id', 'bookAuthor', 'bookName', 'bookDate', 'bookPageCount', 'bookInstances']

admin.site.register(Book, BookAdmin)
class ReaderAdmin(admin.ModelAdmin):
    model = Reader
    list_display = ['id', 'readerFirstName', 'readerSecondName', 'readerBirthday', 'hashPassword']

admin.site.register(Reader, ReaderAdmin)