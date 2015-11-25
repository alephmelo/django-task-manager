from django import forms
from core.models import Task

class TaskForm(forms.ModelForm):
    '''
    Task Form inherits from Django Model Form.

    Fields are: ['due_date', 'title', 'tags']
    '''
    class Meta:
            model = Task
            fields = ['due_date', 'title', 'tags']
            exclude = ('user',)
            widgets = {
            'due_date': forms.TextInput(attrs={
                'id':'flatpickr',
                'placeholder':'Due date',
            }),
            'title': forms.TextInput(attrs={
            	'placeholder':'Task to be done'
            	}),
            'tags': forms.TextInput(attrs={
            	'placeholder':'Eg.: python, django, views'
            	}),
            }

class TaskEditForm(forms.ModelForm):
    '''
    Inherits from Django Model Form

    Fields are: ['due_date', 'title, 'is_complete']
    '''
    class Meta:
            model = Task
            fields = ['due_date', 'title', 'is_complete']
            exclude = ('user', 'tags')
            widgets = {
            'due_date': forms.TextInput(attrs={
                'id':'flatpickr',
                'placeholder':'Due date',
            }),
            'title': forms.TextInput(attrs={
                'placeholder':'Task to be done'
                }),
            }
