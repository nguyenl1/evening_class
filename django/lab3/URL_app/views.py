from django.shortcuts import render, redirect
from .models import UrlForm
from django.http import HttpResponse
import random
import string

def home(request):

    if request.method == "POST":

        site_name = request.POST['site_name']
        url_link = request.POST['url_link']

        
        last = UrlForm.objects.last()
        code = last.short_url()

        latest_en = UrlForm.objects.create(site_name=site_name, url_link=url_link, code=code)

        

    
        return redirect("new_url")
    return render(request, "home.html")


def new_url(request):

    last = UrlForm.objects.last()

    context = {
        'short':last, 
    }

    return render(request, "new_url.html", context=context)

    

def save_url(request):
    return redirect("home")


def view_url(request):
    list_urls = UrlForm.objects.all()

    context = {
        'views':list_urls, 
    
    }
    return render(request,"view_urls.html", context=context)



# if UrlForm.site_name == site_name:
#             UrlForm.objects.get(site_name=site_name)
#             return UrlForm.code 