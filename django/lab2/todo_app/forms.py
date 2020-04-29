from django import forms

from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('Task','text')