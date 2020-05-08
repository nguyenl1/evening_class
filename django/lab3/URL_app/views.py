from django.shortcuts import render
from .models import UrlForm
from django.http import HttpResponse
import random
import string

def home(request):

    if request.method == "POST":

        site_name = request.POST['site_name']
        url_link = request.POST['url_link']

        UrlForm.objects.create(site_name=site_name, url_link=url_link, )

        last = UrlForm.objects.last()
        short = last.url_link
        new_url = last.short_url()

        print (new_url)
    return render(request, "home.html")

def convert(request):

    last = UrlForm.objects.last()
    short = last.short_url()
    short = last.url_link

    print (short)


def save_url(request):
    return redirect("home")


def view_url(request):
    list_urls = UrlForm.objects.all()

    context = {
        'views':list_urls, 
    
    }
    return render(request,"view_urls.html", context=context)

def new_url(request,id):
    pass 

