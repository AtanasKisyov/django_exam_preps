from django.urls import path

from online_library.main.views import home, add_book, edit_book, book_details, profile, edit_profile, delete_profile, \
    delete_book

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_book, name='add_book'),
    path('edit/int:<pk>', edit_book, name='edit_book'),
    path('details/int:<pk>', book_details, name='book_details'),
    path('delete/int:<pk>', delete_book, name='delete_book'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/delete', delete_profile, name='delete_profile'),
]
