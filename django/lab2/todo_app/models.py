from django.db import models

class Task(models.Model):
    task = models.CharField(max_length = 250, blank = False)
