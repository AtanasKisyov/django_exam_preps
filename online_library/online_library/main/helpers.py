from online_library.main.models import Profile, Book


def get_user_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def get_user_books():
    books = Book.objects.all()
    if books:
        return books
    return None
