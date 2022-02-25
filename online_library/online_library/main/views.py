from django.shortcuts import render, redirect

from online_library.main.forms import CreateProfile, CreateBook, EditBook, DeleteBook, EditProfile, DeleteProfile
from online_library.main.helpers import get_user_profile, get_user_books
from online_library.main.models import Book


def home(request):
    user_profile = get_user_profile()
    if user_profile:
        books = get_user_books()
        context = {'books': books}
        template = 'home-with-profile.html'
    else:
        template = 'home-no-profile.html'
        if request.method == 'POST':
            form = CreateProfile(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = CreateProfile()
        context = {'form': form}
    return render(request, template, context)


def add_book(request):
    if request.method == 'POST':
        form = CreateBook(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateBook()
    context = {'form': form}
    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditBook(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditBook(instance=book)
    context = {'form': form}
    return render(request, 'edit-book.html', context)


def book_details(request, pk):
    book = Book.objects.get(pk=pk)
    context = {'book': book}
    return render(request, 'book-details.html', context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    delete_form = DeleteBook(instance=book)
    delete_form.save()
    return redirect('home')


def profile(request):
    user_profile = get_user_profile()
    context = {'user_profile': user_profile}
    return render(request, 'profile.html', context)


def edit_profile(request):
    user_profile = get_user_profile()
    if request.method == 'POST':
        form = EditProfile(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfile(instance=user_profile)
    context = {'form': form}
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    user_profile = get_user_profile()
    if request.method == 'POST':
        form = DeleteProfile(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DeleteProfile(instance=user_profile)
    context = {'form': form}
    return render(request, 'delete-profile.html', context)
