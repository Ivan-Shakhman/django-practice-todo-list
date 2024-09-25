from symtable import Class

from django import forms

from todo_app.models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('content', 'deadline', 'tags')
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)