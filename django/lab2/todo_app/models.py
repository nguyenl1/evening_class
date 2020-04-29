from django.db import models
from django.conf import settings
from django.utils import timezone

class Task(models.Model):
    task_name = models.CharField(max_length = 250, blank = False)
    desp = models.TextField()
    due_date = models.DateTimeField(blank=True, null=True)

