from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model

class TodoItem(models.Model):
    task_name = models.CharField(max_length = 250, blank = False)
    due_date = models.DateTimeField (blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def complete_task(self):
        self.is_completed = True
        return self.is_completed



    

