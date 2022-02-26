from django import forms

from notes.main.models import Profile, Note


class CreateProfile(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfile(forms.ModelForm):

    def save(self, commit=True):
        Note.objects.all().delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = '__all__'


class CreateNote(forms.ModelForm):

    class Meta:
        model = Note
        fields = '__all__'


class EditNote(forms.ModelForm):

    class Meta:
        model = Note
        fields = '__all__'


class DeleteNote(forms.ModelForm):

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Note
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'readonly': 'readonly'}),
            'image_url': forms.TextInput(attrs={'readonly': 'readonly'}),
            'content': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
