from django.urls import path
from note_app import views

urlpatterns = [
    path('', views.NoteListView.as_view(), name="home"),
    path('<int:pk>', views.NoteDetailView.as_view(), name="note_detail"),
    path('/create-post', views.add_note, name="create-post"),
]