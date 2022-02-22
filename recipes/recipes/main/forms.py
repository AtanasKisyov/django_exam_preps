from django import forms

from recipes.main.models import Recipe


class CreateRecipe(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = '__all__'


class EditRecipe(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = '__all__'


class DeleteRecipe(forms.ModelForm):

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'readonly': 'readonly'}),
            'image_url': forms.TextInput(attrs={'readonly': 'readonly'}),
            'description': forms.Textarea(attrs={'readonly': 'readonly'}),
            'ingredients': forms.TextInput(attrs={'readonly': 'readonly'}),
            'time': forms.NumberInput(attrs={'readonly': 'readonly'}),
        }
