from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from .models import Note


class IndexView(generic.ListView):
    template_name = 'notes/index.html'
    context_object_name = 'note_list'
    
    def get_queryset(self):
        return Note.objects.order_by('-pub_date').all()
        
def delete(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    selected_note = note.choice_set.get(pk=request.POST['note'])
    selected_note.delete();
