from django import forms
from core.models import Task

class TaskForm(forms.ModelForm):
	class Meta:
			model = Task
			exclude = ('user',)
			widgets = {
            'due_date': forms.TextInput(attrs={
                'id':'flatpickr'
            }),
            }
