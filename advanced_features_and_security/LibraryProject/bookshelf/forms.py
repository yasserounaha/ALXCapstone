# forms.py in bookshelf

from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'library']

    title = forms.CharField(max_length=200, required=True)
    author = forms.CharField(max_length=100, required=True)
    publication_year = forms.IntegerField(required=True)
    library = forms.ModelChoiceField(queryset=Library.objects.all(), required=True)
