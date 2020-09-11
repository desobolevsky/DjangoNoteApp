from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Note


# Create your views here.
class NoteListView(ListView):
    model = Note
    ordering = ['-date_updated']

    # make users see only their notes
    def get_queryset(self):
        queryset = super(NoteListView, self).get_queryset()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(author=self.request.user)
        else:
            return None
        return queryset


class CreateNoteView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'text']

    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateNoteView(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title', 'text']

    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # restrict users see each other notes
    def get_queryset(self):
        queryset = super(UpdateNoteView, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset


class DeleteNoteView(DeleteView, LoginRequiredMixin):
    model = Note

    success_url = reverse_lazy('home-page')

    # delete without confirmation (template) page
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, *kwargs)

    # restrict users delete each other notes
    def get_queryset(self):
        queryset = super(DeleteNoteView, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset
