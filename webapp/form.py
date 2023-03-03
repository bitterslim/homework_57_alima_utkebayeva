from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models.task import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'status', 'date', 'description')
        labels = {
            'title': 'Task title',
            'status': 'Task status',
            'type': 'Task type',
            'date': 'To do date',
            'description': 'Task description'
        }

    def clean_user(self):
        user = self.cleaned_data.get('user')
        if len(user) < 2:
            raise ValidationError('Your username is short')
        return user
