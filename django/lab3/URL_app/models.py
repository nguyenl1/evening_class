from django.db import models



class UrlForm(models.Model):
    site_name = models.CharField(max_length = 200, blank=True)
    url_link = models.CharField(max_length = 500, blank=False)
    




    
