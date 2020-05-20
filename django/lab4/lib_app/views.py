from django.shortcuts import render, redirect
from .models import Book, Checkout
from django.utils import timezone


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
    book = Book.objects.get(pk=id)
    if request.method == 'POST':
        check = Checkout(request.POST)
        book = check.book = book
        borrower = check.borrower = request.user
        checkout_date = check.checkout_date = timezone.now()
        due_date = check.due()

        Checkout.objects.create(book=book, borrower=borrower, checkout_date=checkout_date, due_date=due_date)

        if request.POST.get('checked_out', False) == "on":
            check.borrowed()

        
        return redirect('list_books')
    return render(request,"lib_app/list_books.html")

def my_books (request):
    books = Checkout.objects.filter(borrower=request.user)
    context = {
        'books':books,
    }
    
    return render(request,'lib_app/my_books.html', context)