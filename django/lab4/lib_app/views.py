from django.shortcuts import render
from .models import Book, Checkout

def home(request):
    return render(request, "lib_app/home.html")

def list_books(request):
    books = Book.objects.all()

    context = {
            'books':books, 
        }

    return render(request,"lib_app/list_books.html", context=context)

def book_details (request,id):
    desp = Book.objects.get(pk=id)

    context = {
        'desp':desp,
    }

    return render(request, "lib_app/book_details.html", context=context)
