from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .models import Book, Reader
def index(request):
    return render(request, 'index.html')

def books_list(request):
    return render(request, 'books.html')

def readers(request):
    return render(request, 'readers.html')

def library(request):
    return render(request, 'library.html')

def bookList(request):
    books = Book.objects.all()
    context = {
        'render_task': books,
        'page_title':'Список книг',
    }
    return render(request, 'books.html', context)

def readersList(request):
    readers = Reader.objects.all()
    context = {
        'render_task': readers,
        'page_title':'Список читателей',
    }
    return render(request, 'library.html', context)