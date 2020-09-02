from django.urls import path
from . import views as page_views

urlpatterns = [
    path('', page_views.home_page, name='home-page'),
    path('create/', page_views.CreateNoteView.as_view(template_name='notesapp/create_note.html'),
         name='create-note-page'),
    path('update/<int:pk>/', page_views.UpdateNoteView.as_view(template_name='notesapp/update_note.html'), name='update-note-page'),
]
