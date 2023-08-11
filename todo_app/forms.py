from django import forms

from todo_app.models import TaskModel


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['task_title', 'task_description']