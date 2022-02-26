from django.urls import path
from notes.main.views import *


urlpatterns = [
    path('', home, name='home'),
    path('add/', add_note, name='add_note'),
    path('edit/int:<pk>', edit_note, name='edit_note'),
    path('delete/int:<pk>', delete_note, name='delete_note'),
    path('details/int:<pk>', note_details, name='note_details'),
    path('profile/', profile, name='profile'),
    path('profile/delete', delete_profile, name='delete_profile'),
]
