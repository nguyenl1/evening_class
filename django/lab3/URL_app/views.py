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

    return render(request, "home.html")

def save_url(request):
    return redirect("home")

def code(request):
    new = string.ascii_letters + string.digits

    i = ""
    y = 0
    while 0 <= 6:
        y = y + 1
        i += random.choice(new)
        if y == 6:
            break

    new_url = i 

    print("https://www.myurl.com/" + f"{new_url}")

    pass 

def view_url(request):
    list_urls = UrlForm.objects.all()

    context = {
        'views':list_urls, 
    
    }
    return render(request,"view_urls.html", context=context)

