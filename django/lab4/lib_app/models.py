from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.conf import settings 

class Book(models.Model):
    author = models.CharField(max_length = 200)
    title = models.CharField(max_length = 200)
    desp = models.TextField(max_length = 2000, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Checkout(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null = True)
    borrower = models.ForeignKey(get_user_model(), on_delete= models.SET_NULL, null=True, blank=True)
    checkout_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(blank=True, null=True)
    checked_out = models.BooleanField(default=False)

    def borrowed(self):
        self.checked_out = True
        return self.checked_out

   