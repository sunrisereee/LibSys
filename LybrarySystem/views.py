from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

def index(request):
    return render(request, 'index.html')

def books_list(request):
    return render(request, 'books.html')

def readers(request):
    return render(request, 'readers.html')

def library(request):
    return render(request, 'library.html')