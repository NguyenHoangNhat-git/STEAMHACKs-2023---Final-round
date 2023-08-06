from .models.journal import Note
from django import forms
import datetime

class JournalForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ("__all__")