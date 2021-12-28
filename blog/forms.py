from django import forms
from django.core.exceptions import ValidationError

from .models import Article


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Категория не выбрана"
        self.fields['writer'].empty_label = "Писатель не выбран"

    class Meta:
        model = Article
        fields = ['title', 'slug', 'content', 'category', 'writer']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        """Валидация для поля title"""
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError('Длина превышает 50 символов')

        return title
