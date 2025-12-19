from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'title', 'note'
        ]

    widgets = {
        'title': forms.TextInput(attrs={
            'class':'input',
            'placeholder': 'Enter title',
        }),
        'note':forms.TextInput(attrs={
            'class':'textarea',
            'placeholder': 'Write your notes here...',
            'rows':5
        })
    }
