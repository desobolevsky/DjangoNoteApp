from django.urls import path
from . import views as page_views

urlpatterns = [
    path('', page_views.home_page, name='home-page'),
    path('create/', page_views.CreateNoteView.as_view(template_name='notesapp/create_note.html'),
         name='create-note-page')
]
