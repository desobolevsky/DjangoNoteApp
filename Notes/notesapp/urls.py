from django.urls import path
from . import views as page_views

urlpatterns = [
    path('', page_views.home_page, name='home-page'),
    path('create/', page_views.CreateNoteView.as_view(template_name='notesapp/create_note.html'),
         name='create-note-page'),
    path('<int:pk>/', page_views.UpdateNoteView.as_view(template_name='notesapp/update_note.html'),
         name='update-note-page'),
    path('delete/<int:pk>', page_views.DeleteNoteView.as_view(template_name='notesapp/delete_note.html'),
         name='delete-note-page'),
]
