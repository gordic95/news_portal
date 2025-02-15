from django import forms
from .models import Post




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author']

        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control'}),
        #     'author': forms.Select(attrs={'class': 'form-control'}),
        #     'category': forms.Select(attrs={'class': 'form-control'}),
        # }

        def clean(self):
            cleaned_data = super().clean()
            print(cleaned_data)
            description = cleaned_data.get('title')
            print(description)
            if len(description) < 3:
                raise forms.ValidationError('Слишком короткий заголовок')
            return cleaned_data

