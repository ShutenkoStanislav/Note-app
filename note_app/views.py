from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from note_app import models
from note_app.forms import NoteForm

class NoteListView(ListView):
    model = models.Note
    context_object_name = "notes"
    template_name = "notes/note_list.html"

class NoteDetailView(DetailView):
    model = models.Note
    context_object_name = "note"
    template_name = "notes/note_detail.html"

def add_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm()
    return render(request, "notes/add_note.html", {'form': form})

