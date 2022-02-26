from django.shortcuts import render, redirect

from notes.main.forms import CreateProfile, CreateNote, EditNote, DeleteNote, DeleteProfile
from notes.main.helpers import get_user_profile, get_notes
from notes.main.models import Note


def home(request):
    user_profile = get_user_profile()
    notes = get_notes()
    template = ''
    context = {}
    if not user_profile:
        if request.method == 'POST':
            form = CreateProfile(request.POST, instance=user_profile)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = CreateProfile()
            template = 'home-no-profile.html'
            return render(request, template, {'form': form})
    else:
        template = 'home-with-profile.html'
        context = {
            'notes': notes
        }
    return render(request, template, context)


def add_note(request):
    if request.method == 'POST':
        form = CreateNote(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateNote()
    context = {'form': form}
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNote(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditNote(instance=note)
    context = {'form': form}
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteNote(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DeleteNote(instance=note)
    context = {'form': form}
    return render(request, 'note-delete.html', context)


def note_details(request, pk):
    note = Note.objects.get(pk=pk)
    context = {'note': note}
    return render(request, 'note-details.html', context)


def profile(request):
    user_profile = get_user_profile()
    notes_count = Note.objects.all().count()
    context = {'user_profile': user_profile, 'notes_count': notes_count}
    return render(request, 'profile.html', context)


def delete_profile(request):
    user_profile = get_user_profile()
    delete_form = DeleteProfile(instance=user_profile)
    delete_form.save()
    return redirect('home')
