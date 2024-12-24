# forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']  # Add 'due_date' here
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # Use datetime-local input for user-friendly date selection
        }
