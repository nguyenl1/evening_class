from django.shortcuts import render, redirect, get_object_or_404
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
    
    if request.method == 'POST':
            
        check = Checkout(request.POST)
        book = Book.objects.get(id=id)
        # book = check.book = book
        borrower = check.borrower = request.user
        checkout_date = check.checkout_date = timezone.now()
        due_date = check.due()
        status = 'u'

        

        print(f'''
        check: {check}
        book: {book}
        borrower: {borrower}
        due_date: {due_date}
        status: {status}
        ''')

        Checkout.objects.create(book_id=book, borrower=borrower, checkout_date=checkout_date, due_date=due_date, status=status)
        
        return redirect('my_books')
    return render(request,"lib_app/list_books.html")

def my_books (request):
    books = Checkout.objects.filter(borrower=request.user)
    context = {
        'books':books,
    }
    
    return render(request,'lib_app/my_books.html', context)
    

def return_book(request,id):
    avail = Checkout.objects.get(pk=id)
    avail.status = 'a'
    avail.borrower = None
    avail.checkout_date = None 
    avail.save()
    # if request.POST.get('status') == 'u':
        

    return redirect('my_books')



    

