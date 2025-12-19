from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm

# Create your views here.


def index(request):
    return render(request, 'note/index.html')

@login_required
def show_notes(request):
    notes = Note.objects.filter(user=request.user).order_by('-date_created')
    context = {
        'notes':notes,
    }
    return render(request, 'note/show_notes.html', context)

@login_required
def note_detail(request, note_id):
    note = Note.objects.get(id=note_id, user=request.user)
    return render(request, 'note/note_detail.html', {'note': note})

@login_required
def add_notes(request):
    # Submit filled form
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.user = request.user
            new_note.save()
            return redirect('note:show_notes')
    else:
        # Create empty form
        form = NoteForm()
    context = {
        'form':form,
    }
    return render(request, 'note/add_notes.html', context )

@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note:show_notes')
    else:
        form = NoteForm(instance=note)
    context = {
        'form':form
    }

    return render(request, 'note/edit_note.html',  context)

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('note:show_notes')
    
    return render(request, 'note/delete_note.html', {'note':note})



