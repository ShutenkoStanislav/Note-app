from django import forms
from note_app.models import Note

class NoteForm(forms.Model):
    model = Note
    fields = ["title", "content"]