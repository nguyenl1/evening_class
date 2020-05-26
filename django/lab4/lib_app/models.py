from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.conf import settings 
from dateutil.relativedelta import relativedelta

class Book(models.Model):
    author = models.CharField(max_length = 200)
    title = models.CharField(max_length = 200)
    desp = models.TextField(max_length = 2000, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Checkout(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.SET_NULL, null = True)
    borrower = models.ForeignKey(get_user_model(), on_delete= models.SET_NULL, null=True, blank=True)
    checkout_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)

    LOAN_STATUS = (
        ('a', 'available'),
        ('u', 'unavailable'),
    )

    status = models.CharField(
        max_length = 1,
        choices = LOAN_STATUS,
        blank = True,
        default = 'a',
        help_text= 'book availability', 
    )
    
    def due(self):
        self.due_date = self.checkout_date + relativedelta(weeks=2)
        return self.due_date

   