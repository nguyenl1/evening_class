from django.shortcuts import render, redirect
from .models import UrlForm
from django.http import HttpResponse
import random
import string

def home(request):
    if request.method == "POST":

        url_link = request.POST['url_link']

        copy = UrlForm.objects.filter(url_link = url_link) 
        if copy.exists():
            return render(request, "copy_url.html", {"copy":copy})


    elif request.method == "POST":

        site_name = request.POST['site_name']
        url_link = request.POST['url_link']

        last = UrlForm.objects.last()
        code = last.short_url()

        UrlForm.objects.create(site_name=site_name, url_link=url_link, code=code)

        return redirect("new_url")


    else:
        return render(request, "home.html")

        

    
    


def new_url(request):

    last = UrlForm.objects.last()

    context = {
        'short':last, 
    }

    return render(request, "new_url.html", context=context)


def view_url(request):
    list_urls = UrlForm.objects.all()

    context = {
        'views':list_urls, 
    
    }
    return render(request,"view_urls.html", context=context)

# def copy_url(request,id):
#     copy = UrlForm.objects.filter(url_link = url_link)

#     if copy.exists():

#         context = {
#             'copy':copy,
#         }

#         return render(request, "copy_url.html", context=context)