from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from note_app import models
from note_app.forms import NoteForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

class NoteListView(ListView):
    model = models.Note
    context_object_name = "notes"
    template_name = "notes/home_page.html"

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

# @login_required
# def profile(request):
#     context = {
#         "user" : request.user,
#     }
#     return render(
#         request,
#         "notes/profile.html",
#         context,
#     )

    

