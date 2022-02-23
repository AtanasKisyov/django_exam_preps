from django import forms

from online_library.main.models import Profile, Book


class CreateProfile(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'


class CreateBook(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'


class EditBook(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'


class DeleteBook(forms.ModelForm):

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Book
        fields = '__all__'
