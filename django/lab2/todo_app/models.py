from django.db import models

class Tasks(models.Model):
    tasks = models.CharField(max_length = 250, blank = False)
