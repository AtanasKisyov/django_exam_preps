from django import forms

from online_library.main.models import Profile, Book


class CreateProfile(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'


class EditProfile(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfile(forms.ModelForm):

    def save(self, commit=True):
        Book.objects.all().delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'last_name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'image_url': forms.TextInput(attrs={'readonly': 'readonly'}),
        }


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
