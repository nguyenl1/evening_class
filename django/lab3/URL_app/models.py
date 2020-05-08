from django.db import models
import random
import string



class UrlForm(models.Model):
    site_name = models.CharField(max_length = 200, blank=True)
    code = models.CharField(max_length = 10, blank=True)
    url_link = models.CharField(max_length = 500, blank=False)

    def short_url(self):

        new = string.ascii_letters + string.digits

        i = ""
        y = 0
        while 0 <= 6:
            y = y + 1
            i += random.choice(new)
            if y == 6:
                break
        
        # new_url = "https://www.myurl.com/" + f"{i}"

        self.code = i
        
        return self.code




    
