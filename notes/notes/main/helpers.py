from django.shortcuts import redirect, render

from notes.main.models import Profile, Note


def get_user_profile():
    user_profile = Profile.objects.all()
    if user_profile:
        return user_profile[0]
    return None


def get_notes():
    notes = Note.objects.all()
    if notes:
        return notes
    return None


def form_handle(request, django_form, instance, template, success_url):
    if request.method == 'POST':
        form = django_form(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = django_form(instance=instance)
    context = {'form': form}
    return render(request, template, context)
