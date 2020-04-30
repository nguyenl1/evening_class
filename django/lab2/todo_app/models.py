from django.db import models
from django.conf import settings

class Task(models.Model):
    task_name = models.CharField(max_length = 250, blank=True, null=True)
    desp = models.TextField()
    due_date = models.CharField(max_length = 250, blank=True, null=True)

    def __str__(self):
        return self.task_name