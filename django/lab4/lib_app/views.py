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

def checked_out (request,id):
    borrowed = Checkout.objects.get(pk=id)

    if request.POST.get('checked_out', False) == "on":
        borrowed.borrowed()
        borrowed.save()

        return redirect('list_books')

def my_books (request):
    pass 