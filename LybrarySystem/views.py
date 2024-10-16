from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Book, Reader

def index(request):
    return render(request, 'index.html')

def books_list(request):
    return render(request, 'books.html')
  
@login_required
def readers(request):
    return render(request, 'readers.html')
@login_required
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

@login_required
def addReader(request):
    rSecondName = request.POST.get("last_name")
    rFirstName = request.POST.get("first_name")
    rBirthday = request.POST.get("birth_date")
    # rBirthday = request.POST.get("birth_date")
    newReader = Reader(readerSecondName=rSecondName,readerFirstName=rFirstName,readerBirthday=rBirthday)
    newReader.save()
    return HttpResponseRedirect("/library/library")

@login_required
def editReader(request, id): # МОГУТ БЫТЬ ПРОБЛЕМЫ
    # reader = Reader.objects.get(id=request.POST.get("id"))
    # reader.readerSecondName = request.POST.get("last_name")
    # reader.readerFirstName = request.POST.get("first_name")
    # reader.readerBirthday = request.POST.get("birth_date")
    # reader.save()
    return render(request, 'readerEdit.html', {'reader_id': id})

def editReaderf(request, id):
    reader = Reader.objects.get(id=id)
    reader.readerSecondName = request.POST.get("last_name")
    reader.readerFirstName = request.POST.get("first_name")
    reader.readerBirthday = request.POST.get("birth_date")
    reader.save()
    return HttpResponseRedirect("/library/library")
@login_required
def deleteReader(request): # МОГУТ БЫТЬ ПРОБЛЕМЫ
    Reader.objects.get(id=request.POST.get("id")).delete()
    return HttpResponseRedirect("/LybrarySystem/library")

@login_required
def addBook(request):
    bAuthor = request.POST.get("author")
    bName = request.POST.get("title")
    bDate = request.POST.get("year")
    bPageCount = request.POST.get("pages")
    bInstances = request.POST.get("instances")
    newBook = Book(bookAuthor = bAuthor,bookName = bName,bookDate = bDate,
                        bookPageCount = bPageCount,bookInstances =bInstances)
    newBook.save()
    return HttpResponseRedirect("/library/books")

@login_required
def editBook(request, id): # МОГУТ БЫТЬ ПРОБЛЕМЫ
    # book = Book.objects.get(id=request.POST.get("id"))
    # book.bookAuthor = request.POST.get("author")
    # book.bookName = request.POST.get("title")
    # book.bookDate = request.POST.get("year")
    # book.bookPageCount = request.POST.get("pages")
    # book.bookInstances = request.POST.get("instances")
    # book.save()
    return render(request, 'booksEdit.html', {'book_id': id})

def editBookf(request, id):
    book = Book.objects.get(id=id)
    book.bookAuthor = request.POST.get("author")
    book.bookName = request.POST.get("title")
    book.bookDate = request.POST.get("year")
    book.bookPageCount = request.POST.get("pages")
    book.bookInstances = request.POST.get("instances")
    book.save()
    return HttpResponseRedirect("/library/books")
@login_required
def deleteBook(request): # МОГУТ БЫТЬ ПРОБЛЕМЫ
    Book.objects.get(id=request.POST.get("id")).delete()
    return HttpResponseRedirect("/library/books")

def returnBook(request):
    return HttpResponseRedirect("/library/")

def issueBook(request):
    return HttpResponseRedirect("/library/")
