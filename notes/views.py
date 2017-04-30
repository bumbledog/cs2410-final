from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Note

class IndexView(generic.ListView):
    template_name = 'notes/index.html'
    context_object_name = 'note_list'
    
    def get_queryset(self):
        return Note.objects.order_by('-pub_date').all()

class DetailView(generic.DetailView):
    model = Note
    template_name = 'notes/edit.html'
    
    
def delete(request, note_id):
    note = get_object_or_404(Note, pk=note_id).delete()
    return HttpResponseRedirect(reverse('notes:index'))
    
def add(request):
    title = request.POST.get("title", "")
    content = request.POST.get("content", "")
    newNote = Note(note_title = title, note_content=content, pub_date = timezone.now())
    newNote.save()
    return HttpResponseRedirect(reverse('notes:index'))
    
def change(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.note_title = request.POST.get("title", "")
    note.note_content = request.POST.get("content", "")
    note.save()
    return HttpResponseRedirect(reverse('notes:index'))
