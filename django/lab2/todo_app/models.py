from django.db import models
from django.conf import settings

class Task(models.Model):
    task_name = models.CharField(max_length = 250, blank=True, null=True)
    due_date = models.CharField(max_length = 250, blank=True, null=True)
    is_completed = models.BooleanField(default= False)

    def complete_task(self):
        self.is_completed = True
        return self.is_completed
