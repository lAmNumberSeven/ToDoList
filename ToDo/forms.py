from django import forms
from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

        widgets = {
            'task': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add task'}),
            'completed': forms.CheckboxInput(attrs={'class': 'checkBox'})
        }
