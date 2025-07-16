from django import forms
from .models import Task
from django.utils.dateparse import parse_date


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']
        wiggets = {
            'due_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'placeholder': 'YYYY-MM-DD'
                }
            ),
        }

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date:
            if isinstance(due_date, str):
                try:
                    return parse_date(due_date)
                except (ValueError, TypeError):
                    raise forms.ValidationError(
                        "Enter a valid date in YYYY-MM-DD format.")
        return due_date
