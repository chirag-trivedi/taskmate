from django import forms
from django.forms import fields
from todolist.models import TaskList

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['task','done']