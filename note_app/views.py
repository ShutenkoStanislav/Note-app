from django.shortcuts import render
from django.views.generic import ListView, DetailView
from note_app import models

class NoteListView(ListView):
    model = models.Note
    context_object_name = "list_notes"
    template_name = "note_list.html"

class NoteDetailView(DetailView):
    model = models.Note
    context_object_name = "detail_notes"
    template_name = "note_detail.html"

