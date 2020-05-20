from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('listbooks/',views.list_books, name="list_books"),
    path('bookdetails/<int:id>', views.book_details, name="book_details"),
    path('checkout/<int:id>', views.checked_out, name="checked_out"),
    path('mybooks/', views.my_books, name="my_books"),
]