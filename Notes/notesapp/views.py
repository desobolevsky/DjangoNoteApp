from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Note


# Create your views here.
def home_page(request):
    if request.user.is_authenticated:
        notes = request.user.note_set.all()
        context = {'notes': notes}
    else:
        context = None
    return render(request, 'notesapp/home.html', context=context)


class CreateNoteView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('home-page')
